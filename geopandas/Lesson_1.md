GeoPandas
---

`GeoPandas` - это библиотека написанная поверх `pandas` и используется для 
гео вычислений, манипулирует `GeoSeries` и `GeoDataFrame` что по структуре
являются полными аналогами `Series` и `DataFrame`, с одним единственным отличием,
это наличие обязательного столбца `geometry` которое хранит в себе геометрию.

---

Получение гео данных в виде `GeoDataFrame` из файла 

```python
import geopandas as gpd
df = gpd.read_file('vector_file.shp')
```

---

Получение из `GeoDataFrame` только требуемых полей

```python
FIELDS = ['field_1', 'field_2']
df = df.filter(FIELDS)
```

---

Получение из `GeoDataFrame` минимальный прямолинейный охват его геометрии

```python
_df_bbox = df.unary_union.convex_hull
```

---

Сохранение `GeoDataFrame` в виде файла с гео данными, при сохранении можно 
указывать специальный параметр, `schema` это словарь который указывает как именно
следует интерпретировать сохраняемые поля, указывать их тип данных и используемую
геометрию.

```python
SCHEMA = {
    "geometry": "Unknown",
    'properties': {
        'field_1': 'int',
        'field_2': 'str',
        'field_3': 'date',
        'field_4': 'str',
        'field_5': 'int',
    }
}
df.to_file('path_to_file', schema=SCHEMA, encoding='utf-8')
```
