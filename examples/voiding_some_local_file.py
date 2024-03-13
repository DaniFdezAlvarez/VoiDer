from voider import Voider
from shexer.consts import TURTLE

voider = Voider(
    dataset_URI="http://example.org/shexer/t_graph_1",
    url_graph_input="https://raw.githubusercontent.com/DaniFdezAlvarez/shexer/master/test/t_files/t_graph_1.ttl",
    input_format=TURTLE)

print(voider.gen_void())
