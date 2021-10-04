fn main() {
	let a = vec![1, 2];
	let b = vec![3, 4];
	let ans = Solution::find_median_sorted_arrays(a, b);
	println!("{:?}", ans);
}

pub struct Solution;

impl Solution {
    pub fn find_median_sorted_arrays(nums1: Vec<i32>, nums2: Vec<i32>) -> f64 {
        // Definitely not O(log(n+m)) time, lol, but it's something.
        let n = nums1.len();
        let m = nums2.len();
        let mut mark: usize = (n+m) / 2 - 1;
        if (n+m) % 2 == 0 {
        	mark += 1;
        }

        let mut i: usize = 0;
        let mut j: usize = 0;
        let mut merged: Vec<i32> = Vec::new();
        let mut cnt = 0;
        while i < n && j < m {
        	if nums1[i] < nums2[j] {
        		merged.push(nums1[i]);
        		i += 1;
        	} else {
        		merged.push(nums2[j]);
        		j += 1;
        	}
        	cnt += 1;
        	if cnt == mark + 1 {
        		break;
        	}
        }
        while i < n {
            merged.push(nums1[i]);
        	i += 1;
        	cnt += 1;
        	if cnt == mark + 1 {
        		break;
        	}
        }
        while j < m {
            merged.push(nums2[j]);
        	j += 1;
            cnt += 1;
        	if cnt == mark + 1 {
        		break;
        	}
        }
        if (n+m) % 2 == 0 {
            return ((merged[mark-1] + merged[mark]) / 2) as f64;
        }
        return merged[mark] as f64;
    }
}