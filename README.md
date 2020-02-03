# ViUR base

**WARNING: THIS IS AN UNSTABLE PYTHON3 / PYODIDE PORT, WORK IN PROGRESS!**

**viur-base** provides a basic ViUR project structure.

This is the best place to start a new ViUR 3 project from!

---

## Usage

To setup your new ViUR project, perform these steps:

1. `git clone https://github.com/viur-framework/viur-base.git YOUR-PROJECT`
2. `cd YOUR-PROJECT`
3. `./clean-base.py -A YOUR-APP-ID`
4. `./viur-gcloud-setup.py YOUR-APP-ID` (this step will be improved later!)


When finished, your repository is disconnected from [viur-base](https://github.com/viur-framework/viur-base) as its origin, and can be configured to point to another origin where your new project lives in future. It still contains the full history of the base repository. This might be wanted or not. Do `rm -rf .git` to drop the entire history and start over setting up a clean project with `git init`.

---

### Switch sub-modules to SSH

**WARNING: Not updated to ViUR 3 right now!!!**

Especially in ViUR development projects or for customer projects created at [Mausbrand](https://www.mausbrand.de/en) that are heavily involved in changes to server and vi, it is necessary to change the HTTPS submodules to SSH. This can easily be done for all submodules and their submodules with these few commands:

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
pushd sources/less/ignite
git remote set-url origin git@github.com:viur-framework/ignite.git
popd
```

---

## Contributing

We take a great interest in your opinion about ViUR. We appreciate your feedback and are looking forward to hear about your ideas. Share your visions or questions with us and participate in ongoing discussions.

- [ViUR website](https://www.viur.dev)
- [#ViUR on freenode IRC](https://webchat.freenode.net/?channels=viur)
- [ViUR on GitHub](https://github.com/viur-framework)
- [ViUR on Twitter](https://twitter.com/weloveViUR)

---

## Credits

ViUR is developed and maintained by [Mausbrand Informationssysteme GmbH](https://www.mausbrand.de/en), from Dortmund in Germany. We are a software company consisting of young, enthusiastic software developers, designers and social media experts, working on exciting projects for different kinds of customers. All of our newer projects are implemented with ViUR, from tiny web-pages to huge company intranets with hundreds of users.

Help of any kind to extend and improve or enhance this project in any kind or way is always appreciated.

---

## License

Copyright (C) 2012-2020 by Mausbrand Informationssysteme GmbH.

Mausbrand and ViUR are registered trademarks of Mausbrand Informationssysteme GmbH.

You may use, modify and distribute this software under the terms and conditions of the GNU Lesser General Public License (LGPL). See the file LICENSE provided within this package for more information.
