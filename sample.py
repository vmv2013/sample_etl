import os
import copy
import json
import avro
from avro.datafile import DataFileWriter, DataFileReader
from avro.io import DatumWriter, DatumReader
from pandas import DataFrame

file_path = 'C:/Users/xxx/Desktop/test.avro'
# Read data from an avro file
with open(file_path, 'rb') as f:
    reader = DataFileReader(f, DatumReader())
    metadata = copy.deepcopy(reader.meta)
    schema_from_file = json.loads(metadata['avro.schema'])
    records = [record for record in reader]
    df = DataFrame.from_records(records)
    reader.close()

#print(f'Schema that we specified:\n {schema}')
#print(f'Schema that we parsed:\n {schema_from_file}')
df['complex_map'][0]['key']['c']
