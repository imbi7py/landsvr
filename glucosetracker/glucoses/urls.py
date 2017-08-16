from django.conf.urls import patterns, url

from .views import (
    import_data,
    filter_view,
    quick_add,
    stats_json,
    chart_data_json,
    my_json,
    my_figure,
    GlucoseChartsView,
    GlucoseCreateView,
    GlucoseUpdateView,
    GlucoseDeleteView,
    GlucoseEmailReportView,
    GlucoseListJson,
)

urlpatterns = patterns('',
                       url(
                           regex=r'^import/',
                           view=import_data,
                           name='glucose_import',
                       ),
                       url(
                           regex=r'^filter/',
                           view=filter_view,
                           name='glucose_filter',
                       ),
                       url(
                           regex=r'^quick_add/',
                           view=quick_add,
                           name='glucose_quick_add',
                       ),
                       url(
                           regex=r'^add/',
                           view=GlucoseCreateView.as_view(),
                           name='glucose_create',
                       ),
                       url(
                           regex=r'^list_json/$',
                           view=GlucoseListJson.as_view(),
                           name='glucose_list_json',
                       ),
                       url(
                           regex=r'^chart_data_json/$',
                           view=chart_data_json,
                           name='chart_data_json',
                       ),
                       url(
                           regex=r'^my_json/$',
                           view=my_json,
                           name='my_json',
                       ),
                       url(
                           regex=r'^my_figure/$',
                           view=my_figure,
                           name='my_figure',
                       ),
                       url(
                           regex=r'^stats_json/$',
                           view=stats_json,
                           name='stats_json',
                       ),
                       url(
                           regex=r'^charts/$',
                           view=GlucoseChartsView.as_view(),
                           name='glucose_charts',
                       ),
                       url(
                           regex=r'^email_report/',
                           view=GlucoseEmailReportView.as_view(),
                           name='glucose_email_report',
                       ),
                       url(
                           regex=r'^(?P<pk>\d+)/edit/',
                           view=GlucoseUpdateView.as_view(),
                           name='glucose_update',
                       ),
                       url(
                           regex=r'^(?P<pk>\d+)/delete/',
                           view=GlucoseDeleteView.as_view(),
                           name='glucose_delete',
                       ),
                       )