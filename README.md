# Final-Project-Template
<!-- Edit the title above with your project title -->

## Project Overview

## Self Assessment and Reflection



### Self Assessment
<!-- Replace the (...) with your score -->

| Category          | Score    |
| ----------------- | -------- |
| **Setup**         | 10 / 10 |
| **Execution**     | 20 / 20 |
| **Documentation** | 10 / 10 |
| **Presentation**  | 30 / 30 |
| **Total**         | 70 / 70 |

### Reflection

#### What went well?
When the datasets (IMDb, Netflix, and TMDB) didn’t match well using clean shared keys, I didn’t force them to combine incorrectly. Instead, I changed the approach and adjusted the analysis so it could work with the data properly without creating errors.

#### What did not go well?
I wasted too much time trying to fix a merge that was impossible. In the future, I will check if my files can actually be merged before I start working on them, so I don't waste time later.

#### What did you learn?
I learned how to use Git/GitHub and how to build machine learning pipelines. Most importantly, I learned that it is okay to admit when data doesn't fit together. Identifying limitations in your data is just as important as getting good results from the model.

#### What would you do differently next time?
Next time, I will check if my datasets fit together as soon as I load them. I will also make sure to leave extra time in my schedule in case I have to change my plan again, so I don't feel rushed at the end.
---

## Getting Started
### Installing Dependencies

To ensure that you have all the dependencies installed, and that we can have a reproducible environment, we will be using `pipenv` to manage our dependencies. `pipenv` is a tool that allows us to create a virtual environment for our project, and install all the dependencies we need for our project. This ensures that we can have a reproducible environment, and that we can all run the same code.

```bash
pipenv install
```

This sets up a virtual environment for our project, and installs the following dependencies:

- `ipykernel`
- `jupyter`
- `notebook`
- `black`
  Throughout your analysis and development, you will need to install additional packages. You can can install any package you need using `pipenv install <package-name>`. For example, if you need to install `numpy`, you can do so by running:

```bash
pipenv install numpy
```

This will update update the `Pipfile` and `Pipfile.lock` files, and install the package in your virtual environment.

## Helpful Resources:
* [Markdown Syntax Cheatsheet](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
* [Dataset options](https://it4063c.github.io/guides/datasets)
