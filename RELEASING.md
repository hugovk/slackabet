# Release Checklist

- [ ] Get main to the appropriate code release state.
      [GitHub Actions](https://github.com/hugovk/slackabet/actions) should be running
      cleanly for all merges to main.
      [![GitHub Actions status](https://github.com/hugovk/slackabet/workflows/Test/badge.svg)](https://github.com/hugovk/slackabet/actions)

- [ ] Edit release draft, adjust text if needed:
      https://github.com/hugovk/slackabet/releases

- [ ] Check next tag is correct, amend if needed

- [ ] Publish release

- [ ] Check the tagged
      [GitHub Actions build](https://github.com/hugovk/slackabet/actions?query=workflow%3ADeploy)
      has deployed to [PyPI](https://pypi.org/project/slackabet/#history)

- [ ] Check installation:

```bash
pip3 uninstall -y slackabet && pip3 install -U slackabet && slackabet --version
```
