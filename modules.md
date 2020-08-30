# KSP Modules

Managing KSP modules is best done via the Comprehensive Kerbal Archive Network
(CKAN). It is a package manager for KSP. The command line interface is quite
rich, but it also comes with a `consoleui` that is really helpful when
inspecting new modules.

Unfortunately, many modules aren't maintained anymore, but in many cases, they
still work with newer versions. Module developers often list the module as
supporting up to the current release .9, so it is often necessary to specify
that you want to add other "compatible versions" of KSP to your actual version.
This is particularly necessary with new releases (support 1.9 when 1.10
releases).

## Install and configure ckan

```
brew install ckan
ckan ksp list
ckan compat add 1.9
ckan compat add 1.8
```

## Backup CKAN installed module metapackage

Ckan keeps its current modpack in `ksproot/CKAN/installed-${name}.ckan` (where
`${name}` is the name of the ksp install from `ckan ksp list`. It should be
possible to just copy that file.

An alternate way to backup the modpack is to use the console UI.

1. `ckan consoleui`
2. `F10` (open the menu)
3. Select `Export installed`
4. Copy the resulting file into this repo and commit

## Install Modules

```
ckan install -c *.ckan
```
