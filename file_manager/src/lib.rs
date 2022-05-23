// Python Module
use pyo3::prelude::*;

// Custom
mod constants;
mod file_iterator;
use file_iterator::{iterate_over_files, search_files};
use std::collections::HashMap;

/// Formats the sum of two numbers as string.
#[pyfunction]
fn sum_as_string(a: usize, b: usize) -> PyResult<String> {
    Ok((a + b).to_string())
}

#[pyfunction]
fn get_all_projects() -> PyResult<Vec<HashMap<u16, String>>> {
    Ok(iterate_over_files())
}

#[pyfunction]
fn search_projects(query: &str) -> PyResult<Vec<HashMap<u16, String>>>{
    Ok(search_files(query))
}

/// A Python module implemented in Rust.
#[pymodule]
fn file_manager(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(sum_as_string, m)?)?;
    m.add_function(wrap_pyfunction!(get_all_projects, m)?)?;
    m.add_function(wrap_pyfunction!(search_projects, m)?)?;
    Ok(())
}