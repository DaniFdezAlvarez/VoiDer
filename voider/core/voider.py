
from shexer.shaper import Shaper
from shexer.consts import NT, RDF_TYPE
_VOID_N_ENTITIES = "http://rdfs.org/ns/void#entities"
_VOID_DATASET = "http://rdfs.org/ns/void#Dataset"


class Voider(object):

    def __init__(self,
                 dataset_URI,
                 input_format=NT,
                 graph_file_input=None,
                 graph_list_of_files_input=None,
                 raw_graph=None,
                 url_graph_input=None,
                 rdflib_graph=None,
                 list_of_url_input=None,
                 instantiation_property=RDF_TYPE,
                 compression_mode=None,
                 ):
        self._dataset_uri = dataset_URI

        self._shaper = Shaper(input_format=input_format,
                              graph_file_input=graph_file_input,
                              graph_list_of_files_input=graph_list_of_files_input,
                              raw_graph=raw_graph,
                              url_graph_input=url_graph_input,
                              rdflib_graph=rdflib_graph,
                              list_of_url_input=list_of_url_input,
                              instantiation_property=instantiation_property,
                              compression_mode=compression_mode,
                              all_classes_mode=True
                              )

    def gen_void(self):
        if self._shaper._target_classes_dict is None:
            self._shaper._launch_instance_tracker(verbose=False)
        n_entities = len(self._shaper._target_classes_dict)
        return "\n".join(
            [
             f'<{self._dataset_uri}> <{RDF_TYPE}> <{_VOID_DATASET}> .',
             f'<{self._dataset_uri}> <{_VOID_N_ENTITIES}> {n_entities} .'
            ]
        )



