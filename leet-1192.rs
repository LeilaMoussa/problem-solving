#![allow(unused)]
#![allow(non_upper_case_globals)]

/* https://leetcode.com/problems/critical-connections-in-a-network/ */
/* Probably one of the worst Rust programs I've ever written -- I need to find a cleaner alt to thread_local. */

use std::cmp;
use std::cell::RefCell;
use std::cell::RefMut;

static N: i32 = 4;
thread_local! {
    static stack: RefCell<Vec<i32>> = RefCell::new(vec![]);
    static low: RefCell<Vec<i32>> = RefCell::new(vec![-1; N as usize]);
    static on_stack: RefCell<Vec<bool>> = RefCell::new(vec![false; N as usize]);
    static visited: RefCell<Vec<bool>> = RefCell::new(vec![false; N as usize]);
    static adj_list: RefCell<Vec<Vec<i32>>> = RefCell::new(vec![]);
}

fn main() {
    let n = 4;
    let connections: Vec<Vec<i32>> = vec![vec![0,1],vec![1,2],vec![2,0],vec![1,3]];
    let ans: Vec<Vec<i32>> = Solution::critical_connections(n, connections);
    println!("{:?}", ans);
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
                        Self::dfs(*neighbor);
                    }
                });

                on_stack.with(|on| {
                    if on.borrow()[*neighbor as usize] {
                        low.with(|lo| {
                            let temp = cmp::min(lo.borrow()[current as usize], lo.borrow()[*neighbor as usize]);
                            lo.borrow_mut()[current as usize] = temp;
                        });
                    }
                });
                
                
            }
        });
        
        // We formed our SCC. If we're at the root of the SCC, empty the stack of all members of the SSC.
        low.with(|lo| {
            if lo.borrow()[current as usize] == current {
                stack.with(|s| {
                    while let Some(member) = s.borrow_mut().pop() {
                        on_stack.with(|on| {
                            on.borrow_mut()[member as usize] = false;
                        });
                        if member == current {
                            break;
                        }
                        // I need to understand why this line is necessary, even though we're min-ing
                        lo.borrow_mut()[member as usize] = current;
                    }
                })
            }
        })
    }
    
    pub fn critical_connections(n: i32, connections: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
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
        // By the end, low tells us where the SCCs are, now we need to somehow get the edges
        // that don't link the vertices in those SCCs.
        // Maybe: for each connection, if it connects a vertex from one SCC to another, add it to answer.
        // But that means you need to construct each SCC as a hashset for example
        // No -- vertices in a SCC share low link values, so for each edge, if the vertices have different
        // low links, it's a bridge, so add to ans.
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
