# Generated by Django 3.2.16 on 2022-10-22 18:11

import blog.models
from django.db import migrations
import wagtail.blocks
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.fields
import wagtail.images.blocks
import wagtailmarkdown.blocks


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0021_auto_20221022_1814"),
    ]

    operations = [
        migrations.AlterField(
            model_name="eventpage",
            name="body",
            field=wagtail.fields.StreamField(
                [
                    (
                        "h2",
                        blog.models.Heading2Block(form_classname="title", icon="title"),
                    ),
                    (
                        "h3",
                        blog.models.Heading3Block(form_classname="title", icon="title"),
                    ),
                    (
                        "h4",
                        blog.models.Heading4Block(form_classname="title", icon="title"),
                    ),
                    ("hr", blog.models.HRuleBlock()),
                    (
                        "paragraph",
                        wagtail.blocks.RichTextBlock(
                            features=[
                                "bold",
                                "italic",
                                "underline",
                                "h2",
                                "h3",
                                "h4",
                                "superscript",
                                "subscript",
                                "strikethrough",
                                "ol",
                                "ul",
                                "code",
                                "link",
                                "document-link",
                                "image",
                                "embed",
                            ],
                            icon="pilcrow",
                            label="Paragraph (old)",
                        ),
                    ),
                    (
                        "markdown",
                        wagtailmarkdown.blocks.MarkdownBlock(
                            icon="code", label="Markdown"
                        ),
                    ),
                    ("image", wagtail.images.blocks.ImageChooserBlock()),
                    (
                        "pullquote",
                        wagtail.blocks.StructBlock(
                            [
                                ("quote", wagtail.blocks.TextBlock("quote title")),
                                ("attribution", wagtail.blocks.CharBlock()),
                            ]
                        ),
                    ),
                    (
                        "document",
                        wagtail.documents.blocks.DocumentChooserBlock(
                            icon="doc-full-inverse"
                        ),
                    ),
                    (
                        "code",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "language",
                                    wagtail.blocks.ChoiceBlock(
                                        choices=[
                                            ("bash", "Bash/Shell"),
                                            ("c", "C"),
                                            ("cmake", "CMake"),
                                            ("cpp", "C++"),
                                            ("csharp", "C#"),
                                            ("css", "CSS"),
                                            ("go", "Go"),
                                            ("haskell", "Haskell"),
                                            ("haxe", "Haxe"),
                                            ("html", "HTML"),
                                            ("java", "Java"),
                                            ("js", "JavaScript"),
                                            ("json", "JSON"),
                                            ("kotlin", "Kotlin"),
                                            ("lua", "Lua"),
                                            ("make", "Makefile"),
                                            ("perl", "Perl"),
                                            ("perl6", "Perl 6"),
                                            ("php", "PHP"),
                                            ("python", "Python"),
                                            ("python3", "Python 3"),
                                            ("ruby", "Ruby"),
                                            ("sql", "SQL"),
                                            ("swift", "Swift"),
                                            ("xml", "XML"),
                                        ]
                                    ),
                                ),
                                ("code", wagtail.blocks.TextBlock(rows=15)),
                            ]
                        ),
                    ),
                    (
                        "table",
                        blog.models.HtmlTableBlock(
                            table_options={
                                "autoColumnSize": False,
                                "colHeaders": False,
                                "contextMenu": [
                                    "row_above",
                                    "row_below",
                                    "---------",
                                    "col_left",
                                    "col_right",
                                    "---------",
                                    "remove_row",
                                    "remove_col",
                                    "---------",
                                    "undo",
                                    "redo",
                                ],
                                "editor": "text",
                                "height": 108,
                                "minSpareRows": 0,
                                "renderer": "html",
                                "rowHeaders": False,
                                "startCols": 3,
                                "startRows": 3,
                                "stretchH": "all",
                            }
                        ),
                    ),
                    (
                        "collapsible",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "visible_text",
                                    wagtail.blocks.TextBlock(label="Visible Text"),
                                ),
                                (
                                    "hidden_content",
                                    wagtail.blocks.RichTextBlock(
                                        features=[
                                            "bold",
                                            "italic",
                                            "underline",
                                            "h2",
                                            "h3",
                                            "h4",
                                            "superscript",
                                            "subscript",
                                            "strikethrough",
                                            "ol",
                                            "ul",
                                            "code",
                                            "link",
                                            "document-link",
                                            "image",
                                            "embed",
                                        ],
                                        label="Hidden Content",
                                    ),
                                ),
                            ]
                        ),
                    ),
                    ("callout", blog.models.CalloutBlock()),
                    (
                        "html",
                        wagtail.blocks.StructBlock(
                            [("value", wagtail.blocks.TextBlock(rows=15))]
                        ),
                    ),
                    ("pdf", blog.models.PDFEmbedBlock()),
                    (
                        "embed",
                        wagtail.embeds.blocks.EmbedBlock(max_height=400, max_width=800),
                    ),
                ],
                use_json_field=True,
            ),
        ),
    ]
