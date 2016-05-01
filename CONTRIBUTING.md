# Contributing to Datahub

## Code of Conduct

This project adheres to the Contributor Covenant code of conduct. By participating, you are expected to uphold this code. Please report unacceptable behavior to [datahub@dansloan.org](mailto:datahub@dansloan.org)

## Making Contributions

Contributions from the public are welcome! You can contribute in a number of ways.

### Report Bugs

Report bugs via [Issues](https://github.com/dansdans/datahub/issues).
You can also report errors in documentation in this way as well.

When reporting bugs please make sure to:

 1. Are you actually running up-to-date code? Make sure you have a current (supported) release or a current development version.
 2. Search and make sure someone else hasn't reported the same issue already.
 3. Include relevant details:
    1. Operating system information, including version.
    2. Deployment environment; Python? Virtualenv? Docker image? Dev or production?
    3. *Detailed* steps to reproduce the issue. As much detail as possible, please!

### Fix Bugs

If you are comfortable doing so, go through the Issues list and [create a pull request for](https://help.github.com/articles/creating-a-pull-request/) a bug that you think you can fix. You can feel free to help with anything that is tagged with "bug".

See below for more information on coding style and other information relevant for contributing code to the project.

### Help add features

Help adding features is always welcome, although generally some coordination is needed in many cases. If you are interested in working on a feature, all such Issues are tagged as "feature" - please add a comment to the Issue or contact a core developer directly to discuss it further.

### Write documentation

We could always use more documentation, whether it be adding docstrings to classes and functions in the code, or writing actual documents such as howto guides etc. The best way to go about such a thing is to create an Issue and tag it "doc", then make a pull request and get to work. You can also search for existing "doc" Issues, there might be things we want to get done but haven't gotten around to yet.

### Give feedback

Even if you haven't found any bugs, don't feel comfortable or capable to fix existing bugs or add features or documentation, we still appreciate feedback.

All feedback is welcome, but typically the most constructive feedback is one of the following:

1. A detailed explanation of a new feature you think should be added.
2. An explanation of some source of frustration or poor experience with the project.
3. Any feedback on overall concept/architecture where you feel you have some useful input to offer.

Most problem descriptions or feature proposals should be kept specific and laser-focused. Try to avoid grand sweeping vision features, or at least break it up into a number of smaller more consumable feature proposals.

## Code Contribution Guidelines
### Branching

Datahub uses the [Git-Flow](http://nvie.com/posts/a-successful-git-branching-model/) branching model, in this model all pull requests must be created against the "develop" branch (which is the branch where the next release will be developed). The "master" branch always contains a stable released version, and it is not allowed to submit commits directly to it.

### Pull Request Expectations

#### One thing per PR

A pull request should be clean and contain commits relating only to a specific change. Do not allow other changes to "leak" into your pull request, or it will be rejected. Do not combine several things in one pull request that could reasonably be considered separate (either fixing different bugs, or adding different features, or whatever it might be).

#### Test, test, test, test

The pull request should include tests.

#### Documentation

If the pull request changes functionality, the documentation must be updated as well. At a minimum, docstrings must be updated/added. Preferably, any relevant documentation in /docs should be updated or added.

### Commit Messages

[Follow the seven rules](http://chris.beams.io/posts/git-commit/#seven-rules), summarised here:

1. Separate subject from body with a blank line
2. Limit the subject line to 50 characters
3. Capitalize the subject line
4. Do not end the subject line with a period
5. Use the imperative mood in the subject line
6. Wrap the body at 72 characters
7. Use the body to explain what and why vs. how

Of particular note as something that people often get wrong or forget: use present tense imperative language in (at least) the subject line. In other words:

This is preferred:

```Add a file that does this and that```

This is bad (or at the very least, not preferred):

```Added a file that does this and that```

This is AWFUL and you will go to Git hell:

```This commit is about a file, and I changed something and did this and that```

### Coding Style

Rule of thumb; follow PEP-8. The end (for now).


