# Starpass

**A Python password-utility learning exercise, not a production password manager.**

The CLI generates character strings or checks whether entered text meets
simple composition rules: length, uppercase, lowercase, digit and symbol.

## Run the educational demo

Python 3 and its standard library are sufficient.

```sh
git clone https://github.com/Yuvraj-26-k/Starpass.git
cd Starpass
python Starpassv1.1.py
```

Choose `1` for generation and enter a positive sample length, or `2` to inspect
a disposable example string. Do not type a real password: input is visible.
The actual tracked filename is `Starpassv1.1.py`, including capitalization.

## Important implementation limits

Generation uses Python's ordinary `random` module rather than `secrets`.
**Do not rely on the current generator for real account credentials.** Length
and menu inputs are not robustly validated, and composition checks are not an
entropy estimate, breach check or guarantee of password strength. Generated
strings need not contain every category checked by the separate checker.

The historical screenshot is preserved in the repository but is not embedded
here because it displays password-like input/output. This documentation does
not reproduce those strings, remove the asset, or change Git history.

## Next steps

Replace generation randomness with `secrets`, bound lengths, hide checker input,
separate functions from terminal UI, and add deterministic behavior tests.
There are currently no first-party tests. The wording in this guide describes
the current implementation honestly; the documentation PR does not fix its code
or consolidate this repository with another project.
