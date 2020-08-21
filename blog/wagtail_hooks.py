import wagtail.admin.rich_text.editors.draftail.features as draftail_features
from django.utils.safestring import mark_safe
from wagtail.admin.rich_text.converters.html_to_contentstate import InlineStyleElementHandler
from wagtail.core import hooks


# 1. Use the register_rich_text_features hook.
@hooks.register('register_rich_text_features')
def register_mark_feature(features):
    print("Underline Registered")
    feature_name = 'underline'
    type_ = 'UNDERLINE'
    tag = 'u'

    # 2. Configure how Draftail handles the feature in its toolbar.
    control = {
        'type': type_,
        'icon': ["m 506.83608,162.88809 q -68.85211,2.29506 -90.65526,21.80316 -20.65564,18.36056 -20.65564,83.77007 v 383.27674 q 0,117.04857 40.16372,170.98273 40.16373,52.78661 128.52394,52.78661 102.13064,0 151.47464,-60.81936 49.34401,-60.81936 49.34401,-188.19576 V 276.49406 q 0,-63.11442 -22.9507,-84.91761 -21.80317,-22.9507 -89.50773,-28.68837 v -28.68837 h 252.45771 v 28.68837 q -55.08167,8.03274 -72.29471,27.54084 -17.21302,19.5081 -17.21302,69.99965 v 366.06369 q 0,305.24436 -296.06407,305.24436 -128.52392,0 -212.29399,-60.81937 Q 254.37837,833.0486 233.72273,784.85213 213.0671,736.65565 213.0671,651.73806 V 268.46133 q 0,-61.96691 -17.21303,-80.32745 -16.06549,-19.50812 -76.88484,-25.24579 v -28.68837 h 387.86685 z",
                 "M 170.10924,965.96582 H 891.82756 V 1024 H 170.10924 Z"]
    }

    # 3. Call register_editor_plugin to register the configuration for Draftail.
    features.register_editor_plugin(
        'draftail', feature_name, draftail_features.InlineStyleFeature(control)
    )

    # 4.configure the content transform from the DB to the editor and back.
    db_conversion = {
        'from_database_format': {tag: InlineStyleElementHandler(type_)},
        'to_database_format': {'style_map': {type_: tag}},
    }

    # 5. Call register_converter_rule to register the content transformation conversion.
    features.register_converter_rule('contentstate', feature_name, db_conversion)

    # 6. (optional) Add the feature to the default features list to make it available
    # on rich text fields that do not specify an explicit 'features' list
    features.default_features.append('underline')
