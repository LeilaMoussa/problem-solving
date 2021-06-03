// Is there an even better solution? Probably...

use std::cmp;

impl Solution {
    pub fn get_area(idx_left: usize, idx_right: usize, height_left: i32, height_right: i32) -> i32 {
        cmp::min(height_left, height_right) * (idx_right - idx_left) as i32
    }
    
    pub fn brute_force(height: Vec<i32>) -> i32 {
        // TLE, of course.
        // O(n^2) time, O(1) space
        let mut max_area: i32 = 0;
        for (idx_left, height_left) in height.iter().enumerate() {
            for (idx_right, height_right) in height[idx_left+1..].iter().enumerate() {
                let area: i32 = Solution::get_area(idx_left, idx_right+idx_left+1, *height_left, *height_right);
                if area > max_area {
                    max_area = area;
                }
            }
        }
        max_area
    }
    
    pub fn two_ptrs(height: Vec<i32>) -> i32 {
        // O(n) time, O(1) space
        let mut left = 0;
        let mut right = height.len() - 1;
        let mut max_area: i32 = 0;
        
        while left < right {
            let area = Solution::get_area(left, right, height[left], height[right]);
            if area > max_area {
                max_area = area;
            }
            if height[left] <= height[right] {
                left = left + 1;
            } else {
                right = right - 1;
            }
        }
        max_area
    }
    
    pub fn max_area(height: Vec<i32>) -> i32 {
        //Solution::brute_force(height)
        Solution::two_ptrs(height)
        
    }
}