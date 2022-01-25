from django.core import paginator


class EllipsisPage(paginator.Page):
    def short_page_range(self):
        n = self.paginator.num_pages
        k = self.number
        yield 1
        if k > 3:
            yield 0
        if k > 2:
            yield k - 1
        if k > 1:
            yield k
        if n > k:
            yield k + 1
        if n > k + 2:
            yield 0
        if n > k + 1:
            yield n


class EllipsisPaginator(paginator.Paginator):
    def _get_page(self, *args, **kwargs):
        """
        Return an instance of a single page.

        This hook can be used by subclasses to use an alternative to the
        standard :cls:`Page` object.
        """
        return EllipsisPage(*args, **kwargs)
