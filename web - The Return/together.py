import base64

data = 'eJwtxU0oQ3EAAPD/X7a/t80UzUctWvNQ8pHGyl+SA4flwOwgq83jgINMMyy01PNRwk\
    GRJAcHRS0c3lMje8rXx+s5LLlMzddmUSvtjbbswO/y0zs97mI1SFWe5Mc3wZ/y/yXGAqVM\
    7O7cfqQ5/9fC0zlLs6KVKHKGyTDj7bn/lQy9eDvMVRO1Z/EWrsn9LTe/DwjqH17jCeVZ6v\
    q0yJ6933VtQ0hDG9o+TaHV3j1Dq8+OY9GKW9fHzHTwYvHtiNq5G362tXPsVBDXKCiG0B0e\
    J5aqUzYmddoVUyDiJ7PmydHcA2ak4bSkMeFT7brG1uZerTf8w+XybI60EhKDAMkhgIXSCI\
    KZxozAevNW6ZU+itMcuGxcUCn6ZTBWb0kHIAmwjWb0'

data_bytes = base64.b64decode(data)

import zlib
buffer = zlib.decompress(data_bytes)

with open('flag.7z', 'wb') as flag:
    flag.write(buffer)


`CURSEDNOVA{Home_is_where_the_heart_is}`
