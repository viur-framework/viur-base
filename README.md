# ViUR base

**base** is the ViUR project structure basic repository.

## About

This repository works both as a base structure for new projects created with ViUR, and serves a possibility to generate the quick start ``setup.py`` script, which helps to rapidly setup an empty, new ViUR project without any compromises.

### Using the repository

Download or clone the base repository including its submodules into a new directory of your choice.

When cloning, don't forget to change the remote origin path:

```bash
$ git remote set-url origin git@github.com:USERNAME/REPOSITORY.git
```

### Generating a setup.py

To generate a new setup.py, just call the script ``mksetup.py`` like this:

```bash
$ python mksetup.py >setup.py
```

The setup.py can than be distributed to easily setup new projects from the contents of the ``deploy/`` folder. It automatically downloads the latest ViUR server and pre-compiled vi from the ViUR website to immediately provide a running project.

### Cleaning up with clean-base.py

To make sure that the placeholders in app.yaml and viur_server.py are properly replaced and that you won't accidentally overwrite the viur-base repo, use the included clean-base.py script.

You need to enter an author name and an app ID to identify your app for later deployment and to be able to run the dev_appserver locally.

The script will also initialize and update the submodules and disconnect the repo from the viur-base repository origin.

```base
$ python clean-base.py
```

### Switch sub-modules to SSH

Especially in ViUR development projects or for projects at Mausbrand that are heavily involved in changes to server and vi, it is necessary to change the HTTPS submodules to SSH. This can easily be done for all submodules and their submodules with these few commands:

```bash
# change server
pushd deploy/server
git remote set-url origin git@github.com:viur-framework/server.git
popd

# change vi
pushd vi
git remote set-url origin git@github.com:viur-framework/vi.git
cd html5
git remote set-url origin git@github.com:viur-framework/html5.git
cd ../public/icons
git remote set-url origin git@github.com:viur-framework/icons.git
popd

# change ignite
pushd ignite
git remote set-url origin git@github.com:viur-framework/ignite.git
popd
```

## Contributing

We take a great interest in your opinion about ViUR. We appreciate your feedback and are looking forward to hear about your ideas. Share your visions or questions with us and participate in ongoing discussions.

- [ViUR website](https://www.viur.is)
- [#ViUR on freenode IRC](https://webchat.freenode.net/?channels=viur)
- [ViUR on GitHub](https://github.com/viur-framework)
- [ViUR on Twitter](https://twitter.com/weloveViUR)

## Credits

ViUR is developed and maintained by [Mausbrand Informationssysteme GmbH](https://www.mausbrand.de/en), from Dortmund in Germany. We are a software company consisting of young, enthusiastic software developers, designers and social media experts, working on exciting projects for different kinds of customers. All of our newer projects are implemented with ViUR, from tiny web-pages to huge company intranets with hundreds of users.

Help of any kind to extend and improve or enhance this project in any kind or way is always appreciated.

## License

Copyright (C) 2012-2018 by Mausbrand Informationssysteme GmbH.

Mausbrand and ViUR are registered trademarks of Mausbrand Informationssysteme GmbH.

You may use, modify and distribute this software under the terms and conditions of the GNU Lesser General Public License (LGPL). See the file LICENSE provided within this package for more information.
