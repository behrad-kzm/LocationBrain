from ....domain.entities.RawDataModel import RawDataModel
from xlrd import open_workbook


class ExcelUseCases:

    def extract_models_from_file(self, path: str) -> list[RawDataModel]:
        wb = open_workbook(path)
        models = []
        for sheet in wb.sheets():
            columns = list(sheet._cell_values)
            index_of_location = columns[0].index('Location')
            del columns[0]
            for col in columns:
                location_string = str(list(col)[index_of_location])
                coordination = location_string.split(', ')
                coordination = list(map(float, coordination))
                models.append(RawDataModel(coordination[0], coordination[1], "location"))
        return models
