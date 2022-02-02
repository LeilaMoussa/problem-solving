#![allow(dead_code)]
#![allow(non_upper_case_globals)]
#![allow(unused)]

/// Minimum cost to convert string1 to string2

use std::cmp;

fn main() {
	const string1: &str = "hello";
	const string2: &str = "henlo!";

	let moves_recursive: usize = edit_distance_recursive(string1.get(..), string2.get(..));
	let moves_dp = edit_distance_dp(string1, string2, string1.len(), string2.len());

	assert_eq!(moves_recursive, moves_dp);
}

fn edit_distance_dp(string1: &str, string2: &str, n: usize, m: usize) -> usize {
	let mut dp = vec![vec![0; m+1]; n+1];

	for i in 0..n+1 {
		for j in 0..m+1 {
			if i == 0 {
				dp[i][j] = j;
				// ED(n, m) == m when n == 0
			}
			else if j == 0 {
				dp[i][j] = i;
			}
			else if string1.as_bytes()[i-1] == string2.as_bytes()[j-1] {
				// same last char, trim off the last
				dp[i][j] = dp[i-1][j-1];
			}
			else {
				dp[i][j] = 1 + cmp::min(dp[i-1][j], cmp::min(dp[i][j-1], dp[i-1][j-1]));
			}
		}
	}
	dp[n][m]
}

fn edit_distance_recursive(s1: Option<&str>, s2: Option<&str>) -> usize {
    let string1: &str;
    let string2: &str;

	match s1 {					// not digging this
		Some(x) => string1 = x,
		None => {
			println!("Problemo.");
			return 0;
		}
	}
	match s2 {
		Some(x) => string2 = x,
		None => {
			println!("Problemo.");
			return 0;
		}
	}

	let n: usize = string1.len();
	let m: usize = string2.len();

	if n == 0 {
		return m;
	} else if m == 0 {
		return n;
	}

	if string1.as_bytes()[n-1] == string2.as_bytes()[m-1] { 
		return edit_distance_recursive(string1.get(0..n-1), string2.get(0..m-1));
	}
	return 1 + cmp::min(edit_distance_recursive(string1.get(0..n-1), string2.get(0..m)),
				cmp::min(edit_distance_recursive(string1.get(0..n), string2.get(0..m-1)),
							edit_distance_recursive(string1.get(0..n-1), string2.get(0..m-1))));
}
