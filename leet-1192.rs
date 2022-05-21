#![allow(non_upper_case_globals)]

/* https://leetcode.com/problems/critical-connections-in-a-network/ */

/*
TODOs:
- get accepted on leetcode
- find alternative to thread_local
*/

use std::cmp;
use std::cell::RefCell;
thread_local! {
    static stack: RefCell<Vec<i32>> = RefCell::new(vec![]);
    static low: RefCell<Vec<i32>> = RefCell::new(vec![]);
    static on_stack: RefCell<Vec<bool>> = RefCell::new(vec![]);
    static visited: RefCell<Vec<bool>> = RefCell::new(vec![]);
    static adj_list: RefCell<Vec<Vec<i32>>> = RefCell::new(vec![]);
}

pub struct Solution {}
impl Solution {
    pub fn make_adj_list(mut n: i32, connections: &Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let mut res: Vec<Vec<i32>> = vec![];
        while n > 0 {
            res.push(Vec::new());
            n -= 1;
        }
        for edge in connections.into_iter() {
            res[edge[0] as usize].push(edge[1].to_owned());
            res[edge[1] as usize].push(edge[0].to_owned());
        }
        res
    }
    
    pub fn dfs(current: i32) {
        stack.with(|s| {
            s.borrow_mut().push(current);
            println!("stack: {:?}", s.borrow());
            // Still not quite the behavior we'd like to see -- should empty the stack when an SCC is found
        });

        on_stack.with(|on| {
            on.borrow_mut()[current as usize] = true;
        });

        visited.with(|v| {
            v.borrow_mut()[current as usize] = true;
        });
        
        low.with(|lo| {
            lo.borrow_mut()[current as usize] = current;
        });

        adj_list.with(|adj| {
            for neighbor in adj.borrow()[current as usize].iter() {
                visited.with(|v| {
                    if v.borrow()[*neighbor as usize] == false {
                        // If neighbor is not visited, dfs on it.
                        Self::dfs(*neighbor);
                        // immediately min
                        low.with(|lo| {
                            let temp = cmp::min(lo.borrow()[current as usize], lo.borrow()[*neighbor as usize]);
                            lo.borrow_mut()[current as usize] = temp;
                            println!("lo of current {} was minned with lo of neighbor {}", current, neighbor);
                        });
                    } // else if neighbor is on the stack, low(current) = min( low(current), id(neighbor) )
                    // I have no idea what that means.
                    else {
                        on_stack.with(|on| {
                            if on.borrow()[*neighbor as usize] {
                                low.with(|lo| {
                                    let temp = cmp::min(lo.borrow()[current as usize], *neighbor);
                                    lo.borrow_mut()[current as usize] = temp;
                                    println!("lo of current {} was minned with id of neighbor {}", current, neighbor);
                                });
                            }
                        });
                    }
                });
            }
        });
        
        // We formed our SCC. If we're at the root of the SCC, empty the stack of all members of the SSC.
        low.with(|lo| {
            println!("low: {:?}", lo.borrow());
            if lo.borrow()[current as usize] == current {
                stack.with(|s| {
                    while let Some(member) = s.borrow_mut().pop() {
                        on_stack.with(|on| {
                            on.borrow_mut()[member as usize] = false;
                        });
                        if member == current {
                            break;
                        }
                        //lo.borrow_mut()[member as usize] = current;
                    }
                })
            }
        })
    }
    
    pub fn critical_connections(n: i32, connections: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        if n == 2 {
            return connections;
        }
        
        adj_list.with(|adj| {
            *adj.borrow_mut() = Self::make_adj_list(n, &connections);
        });
        // Tarjan's
        // As long as there are unvisited vertices, dfs from some unvisited vertex
        // In each dfs, push to stack
        for vtx in 0..n {
            visited.with(|v| {
                if v.borrow()[vtx as usize] == false {
                    Self::dfs(vtx);
                }
            });
        }
        
        let mut ans: Vec<Vec<i32>> = vec![];
        for edge in connections.into_iter() {
            low.with(|lo| {
                if lo.borrow()[edge[0] as usize] != lo.borrow()[edge[1] as usize] {
                    ans.push(edge);
                }
            });
        }
        ans
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    fn init_globals(n: i32) {
        low.with(|lo| {
            *lo.borrow_mut() = vec![-1; n as usize];
        });
        on_stack.with(|on| {
            *on.borrow_mut() = vec![false; n as usize];
        });
        visited.with(|vis| {
            *vis.borrow_mut() = vec![false; n as usize];
        });
    }

    #[test]
    fn test_case_1() {
        let n = 4;
        init_globals(n);
        let connections: Vec<Vec<i32>> = vec![vec![0,1],vec![1,2],vec![2,0],vec![1,3]];
        let ans: Vec<Vec<i32>> = Solution::critical_connections(n, connections);
        assert_eq!(ans, [[1, 3]]);
    }

    #[test]
    fn test_case_2() {
        let n = 6;
        init_globals(n);
        let connections: Vec<Vec<i32>> = vec![vec![0,1],vec![1,2],vec![2,0],vec![1,3],vec![3,4],vec![4,5],vec![5,3]];
        let ans: Vec<Vec<i32>> = Solution::critical_connections(n, connections);
        assert_eq!(ans, [[1, 3]]);
    }

    #[test]
    fn test_case_3() {
        let n = 2;
        init_globals(n);
        let connections: Vec<Vec<i32>> = vec![vec![0,1]];
        let ans: Vec<Vec<i32>> = Solution::critical_connections(n, connections);
        assert_eq!(ans, [[0, 1]]);
    }
}
