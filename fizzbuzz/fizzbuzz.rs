// Build:
// $ rustc fizzbuzz.rs
// Run:
// $ ./fizzbuzz

const N: usize = 100;

fn fizzbuzz() -> Vec<String> {
    let mut result: Vec<String> = Vec::with_capacity(N);
    for i in 1..=N {
        result.push(match (i % 3, i % 5) {
            (0, 0) => "FizzBuzz".into(),
            (0, _) => "Fizz".into(),
            (_, 0) => "Buzz".into(),
            (_, _) => i.to_string(),
        })
    }
    result
}

fn main() {
    println!("{:?}", fizzbuzz());
}

// 参考サイト:
// https://gist.github.com/mre/f9e8d31cd1bde76fc714cae3f9d4e131
