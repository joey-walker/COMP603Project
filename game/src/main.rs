/*
COMP603PROJECT:
Dreadnought Khamzhor: Prelude to Space and Time

Authors:
Joey Walker
Deep Patel
Ori Maci
Sarthak Khatiwada
Mentu Singh

*/

use std::io::{self,BufRead};
use std::io::Write;
use std::io::stdout;

//#[derive(Debug)]
/*enum Token<'a> {
	Word(&'a str)

}*/

fn main() {
	let stdin = io::stdin();
	print!("Input text: ");
	stdout().flush();
	let mut inputline = String::new();
	
	stdin.lock().read_line(&mut inputline).unwrap();

	println!("{:?}", inputline);
	tokenize(inputline);
    println!("eof!");
}


fn tokenize<'a>(ourLine: String) -> Vec<'a,&str> {				//-> Vec<Token<'a>> {

	let tokens = ourLine.split(' '); 
	//let mut result = vec![];

	for token in tokens{
		println!("{:?}", token);
		//result.push(Token::Word(token));
	}

	tokens.collect()

}