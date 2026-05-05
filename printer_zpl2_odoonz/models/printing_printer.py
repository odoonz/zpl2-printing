# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import os
from tempfile import mkstemp

from odoo import exceptions, models


class PrintingPrinter(models.Model):
    _inherit = "printing.printer"

    def print_document(
        self, report, content, action=None, doc_format="qweb-pdf", **kwargs
    ):
        """Override to forward doc_format to print_file.

        The base implementation drops doc_format before calling print_file,
        so CUPS never receives the raw flag and treats ZPL as plain text.
        """
        self.ensure_one()
        fd, file_name = mkstemp()
        if isinstance(content, str):
            content = content.encode("utf-8")
        try:
            os.write(fd, content)
        finally:
            os.close(fd)
        try:
            self.print_file(file_name, report=report, doc_format=doc_format, **kwargs)
        except Exception as e:
            raise exceptions.UserError(
                self.env._("Failed to print document: %(error)s", error=e)
            ) from e
        finally:
            try:
                os.remove(file_name)
            except OSError:
                pass
        return True
