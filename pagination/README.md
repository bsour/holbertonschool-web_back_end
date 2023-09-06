# Holberton School Pagination Project

This project provides a Python-based pagination solution for managing and retrieving data from a dataset of popular baby names. It offers a simple way to paginate data with various parameters, including page number and page size. Additionally, it supports hypermedia pagination and deletion-resilient hypermedia pagination.

## Table of Contents

- [Getting Started](#getting-started)
- [Usage](#usage)
- [Tasks](#tasks)
  - [Simple Helper Function](#0-simple-helper-function)
  - [Simple Pagination](#1-simple-pagination)
  - [Hypermedia Pagination](#2-hypermedia-pagination)
  - [Deletion-Resilient Hypermedia Pagination](#3-deletion-resilient-hypermedia-pagination)

## Getting Started

To use this project, you need to have Python 3.7 or higher installed on your system. You should also have the provided dataset file, "Popular_Baby_Names.csv," in the same directory as your Python code.

## Usage

1. Clone the repository to your local machine:

   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:

   ```bash
   cd pagination
   ```

3. Run the desired Python script for the task you want to execute. For example, to run Task 1:

   ```bash
   python 1-simple_pagination.py
   ```

4. Follow the on-screen instructions and examine the output to understand how the pagination works for the given task.

## Tasks

### 0. Simple Helper Function

This task introduces a simple helper function, `index_range`, that calculates the start and end indices for pagination based on page number and page size.

### 1. Simple Pagination

In Task 1, you will implement a `Server` class that allows you to paginate a dataset of popular baby names. It includes a `get_page` method for basic pagination, returning a specific page of data based on page number and page size.

### 2. Hypermedia Pagination

Task 2 extends the `Server` class to support hypermedia pagination. It introduces a `get_hyper` method that provides additional metadata about the paginated data, including the next and previous page numbers.

### 3. Deletion-Resilient Hypermedia Pagination

Task 3 enhances the `Server` class to provide deletion-resilient hypermedia pagination. It introduces a `get_hyper_index` method that ensures users do not miss items from the dataset even if rows are removed between queries.

---
