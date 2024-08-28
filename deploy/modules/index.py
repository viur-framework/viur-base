from viur.core import current, errors, exposed, Module


class Index(Module):

    @exposed
    def index(self, *args, **kwargs):
        """
        This is the final route where every request ends, which was not previously routed elsewhere.
        It normally should provide the landing page of a website, or redirect to a login method,
        depending on the project's use-case.
        """

        # The two lines below ensure that requesting a non-existent module or template throws
        # an error 404 instead of referring to index.
        if len(args) > 1 or kwargs:
            raise errors.NotFound()

        # This manually routes a call to "/sitemap.xml"
        if len(args) == 1 and args[0] == "sitemap.xml":
            return self.sitemap_xml()

        # Else, render index.html
        template = self.render.getEnv().get_template("index.html")
        return template.render()

    @exposed
    def scriptor(self):
        raise errors.Redirect("/scriptor/index.html")

    @exposed
    def sitemap_xml(self, *args, **kwargs):
        current.request.get().response.headers["Content-Type"] = "text/xml"
        return self.render.view({}, tpl="sitemap")
