// Minimum cost to covert string1 to string2

use std::cmp;

fn main() {
	let string1: &str = "hello";
	let string2: &str = "henlow";

	let moves_recursive: usize = edit_distance_recursive(string1.get(..), string2.get(..));
	println!("Total moves {}", moves_recursive);

	// let moves_dp: usize = edit_distance_dp(r1, r2);

	// assert_eq!(moves_recursive, moves_dp);

	// let ascii_moves: usize = edit_distance_ascii(r1, r2);

	// let deletions: usize = edit_distance_deletion(r1, r2);

}

fn edit_distance_recursive(s1: Option<&str>, s2: Option<&str>) -> usize {
    let string1: &str;
    let string2: &str;

	match s1 {
		Some(x) => string1 = x, // reference rather?
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

	if string1.as_bytes()[n-1] == string2.as_bytes()[m-1] {  // same byte representation, i don't care about the actual char
		// aligned so far ==> look before the last characters now
		return edit_distance_recursive(string1.get(0..n-1), string2.get(0..m-1));
	}
	// otherwise, there either needs to be a substitution, deletion, or insertion
	return 1 + cmp::min(edit_distance_recursive(string1.get(0..n-1), string2.get(0..m)),
				cmp::min(edit_distance_recursive(string1.get(0..n), string2.get(0..m-1)),
							edit_distance_recursive(string1.get(0..n-1), string2.get(0..m-1))));
	// cmp::min takes 2 vals
}

// fn edit_distance_dp() {

// }

// fn edit_distance_ascii() {

// }

// fn edit_distance_deletion() {

// }
