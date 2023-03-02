<div align="center">
    <img src="https://github.com/viur-framework/viur-artwork/raw/main/icons/icon-base.svg" height="196" alt="A hexagonal logo of the viur-base" title="viur-base">
    <h1>viur-base</h1>
    <br>
    This is the best place to start a new <a href="https://www.viur.dev">ViUR</a> project from!
</div>

## About

`viur-base` is a template for new ViUR projects and already comes with a default setting to quickly start coding.<br>
The repository is intended to serve as a template, therefore feel free to remove any stuff from it to fit your specific
project demands.

## Requirements

Before you start, please check out the following preliminaries are met:

1. You either need Linux, macOS, or Windows with WSL. See [awesome-viur](https://github.com/viur-framework/awesome-viur#tutorials--examples) for further help and information for specific operating systems.
2. `git`, `python >= 3.10` and `pipenv` should be installed
3. [Google Cloud SDK](https://cloud.google.com/sdk/docs/install) with `app-engine-python` and `app-engine-python-extras` components (see [here](https://docs.viur.dev/latest/start.html#prerequisites) for further help)

## Usage

1. Create a new Google Cloud project [here](https://console.cloud.google.com/projectcreate) and activate billing.
   
    > We will refer to the name of the project you created as `YOUR-APP-ID`.
2. Clone this repository with `git clone https://github.com/viur-framework/viur-base.git YOUR-PROJECT`.

    > This creates a new local folder `YOUR-PROJECT`. In most cases, `YOUR-PROJECT` and `YOUR-APP-ID` should be identical.
3. `cd YOUR-PROJECT`
4. `./clean-base.py -A YOUR-APP-ID`
5. `./viur-gcloud-setup.sh YOUR-APP-ID`
6. Install local development dependencies with `pipenv install --dev`
7. Locally run your project with `pipenv run viur run` or deploy it with `pipenv run viur deploy app`. Run a `pipenv shell` to work with the [viur-cli](https://github.com/viur-framework/viur-cli) command line tool. 

See the [documentation](https://viur-core.readthedocs.io/en/latest/doc_start/index.html) for further help.

## Contributing

ViUR is developed and maintained by [Mausbrand Informationssysteme GmbH](https://www.mausbrand.de/en), from Dortmund in Germany. We are a software company consisting of young, enthusiastic software developers, designers and social media experts, working on exciting projects for different kinds of customers. All of our newer projects are implemented with ViUR, from tiny web-pages to huge company intranets with hundreds of users.

Help of any kind to extend and improve or enhance this project in any kind or way is always appreciated.

We take great interest in your opinion about ViUR. We appreciate your feedback and are looking forward to hear about your ideas. Share your vision or questions with us and participate in ongoing discussions.

## License

Copyright © 2023 by Mausbrand Informationssysteme GmbH.<br>
Mausbrand and ViUR are registered trademarks of Mausbrand Informationssysteme GmbH.

You may use, modify and distribute this software under the terms and conditions of the GNU Lesser General Public License (LGPL).<br>
See the file LICENSE provided within this package for more information.
