use std::collections::BinaryHeap;

/* https://leetcode.com/problems/median-of-two-sorted-arrays/ */

// See median.rs in this repo for a past attempt. This isn't really much better but it looks nicer.

impl Solution {
    pub fn find_median_sorted_arrays(nums1: Vec<i32>, nums2: Vec<i32>) -> f64 {
        // Not fast enough.
        // I think more sophisticated thinking about each of the arrays is needed for opt sol
        
        let n = nums1.len();
        let m = nums2.len();
        
        let mut heap = BinaryHeap::new();
        for elt in nums1.into_iter() {
            heap.push(elt);
        }
        for elt in nums2.into_iter() {
            heap.push(elt);
        }
        // Wait, this isn't that bright -- this is just heapsort, right?
        let v = heap.into_sorted_vec();
    
        if (n+m) % 2 == 0 {
            return (v[(n+m)/2 - 1 as usize] + v[(n+m)/2 as usize]) as f64 / 2.0;
        } else {
            let k = ((n+m)/2) as f64;
            return v[k.ceil() as usize] as f64;
        }
    }
}
