use std::char;

fn main() {
	let x: i32 = 121;
	let ans: bool = Solution::is_palindrome(x);
	println!("{:?}", ans);
}

pub struct Solution;

impl Solution {
    pub fn is_palindrome(x: i32) -> bool {
    	if x == 0 {
    		return true
    	}
        let mut n: i32 = x;
        let mut reverse_string = String::from("");
        while n != 0 {
        	let d = n % 10;
        	let c = char::from_digit(d as u32, 10); // 10 means base 10
        	// I think there's a better way to get the value of an Option
        	match c {
        	    Some(ch) => {
        	        reverse_string.push(ch);
        	    },
        	    None => {}
        	}
        	n /= 10;
        }
        reverse_string == x.to_string()
    }
}