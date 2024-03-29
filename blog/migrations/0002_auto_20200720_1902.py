# Generated by Django 3.0.8 on 2020-07-20 18:02

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.documents.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_squashed_0038_footer_privacy_policy_url"),
    ]

    operations = [
        migrations.AlterField(
            model_name="homepage",
            name="description",
            field=wagtail.fields.StreamField(
                [
                    (
                        "h2",
                        wagtail.blocks.CharBlock(classname="title", icon="title"),
                    ),
                    (
                        "h3",
                        wagtail.blocks.CharBlock(classname="title", icon="title"),
                    ),
                    (
                        "h4",
                        wagtail.blocks.CharBlock(classname="title", icon="title"),
                    ),
                    ("paragraph", wagtail.blocks.RichTextBlock(icon="pilcrow")),
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
                                ("code", wagtail.blocks.TextBlock()),
                            ]
                        ),
                    ),
                ]
            ),
        ),
    ]
