# ViUR base

**base** is the ViUR project structure basic repository.

## About

This repository works both as a base structure for new projects created with ViUR, and serves a possibility to generate the quick start ``setup.py`` script, which helps to quickly setup an empty, new ViUR project without any compromises.

### Using the repository

Download or clone the base repository including its submodules into a new directory of your choice.

When cloning, don't forget to change the remote origin path:

```
git remote set-url origin git@github.com:USERNAME/REPOSITORY.git
```

### Generating a setup.py

To generate a new setup.py, just call the script ``mksetup.py`` like this:

```
python mksetup.py >setup.py
```

The setup.py can than be distributed to easily setup new projects from the contents of the ``deploy/`` folder. It automatically downloads the latest ViUR server and pre-compiled vi from the ViUR website to immediatelly provide a running project.

## Contributing

We take a great interest in your opinion about ViUR. We appreciate your feedback and are looking forward to hear about your ideas. Share your visions or questions with us and participate in ongoing discussions.

- [ViUR on the web](https://www.viur.is)
- [#ViUR on freenode IRC](https://webchat.freenode.net/?channels=viur)
- [ViUR on Google Community](https://plus.google.com/communities/102034046048891029088)
- [ViUR on Twitter](https://twitter.com/weloveViUR)

## Credits

ViUR is developed and maintained by [Mausbrand Informationssysteme GmbH](https://www.mausbrand.de/en), from Dortmund in Germany. We are a software company consisting of young, enthusiastic software developers, designers and social media experts, working on exciting projects for different kinds of customers. All of our newer projects are implemented with ViUR, from tiny web-pages to huge company intranets with hundreds of users.

Help of any kind to extend and improve or enhance this project in any kind or way is always appreciated.

## License

ViUR is Copyright (C) 2012-2017 by Mausbrand Informationssysteme GmbH.

Mausbrand and ViUR are registered trademarks of Mausbrand Informationssysteme GmbH.

You may use, modify and distribute this software under the terms and conditions of the GNU Lesser General Public License (LGPL). See the file LICENSE provided within this package for more information.
