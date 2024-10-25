import json
import os

# JSON 파일을 불러오는 함수
def loadMapJsonData(mapName):
    # 현재 스크립트의 절대 경로를 구합니다
    base_path = os.path.dirname(os.path.abspath(__file__))

    # 타일맵 파일의 절대 경로를 만듭니다
    stage_file_path = os.path.join(base_path, '..', 'static', 'maps', (mapName + '.json'))
    
    stage_data = ''
    try:
        print(f"Loading Map(json) data from: {stage_file_path}")
        with open(stage_file_path, 'r') as stage_file:
            stage_data = json.load(stage_file)
    except FileNotFoundError as e:
        print(f"Stage file not found: {e}")
    except json.JSONDecodeError as e:
        print(f"Error decoding stage JSON: {e}")

    return stage_data


def loadMapTilesetsData():
    # 타일셋 데이터 정의 (파일이 아닌 경로 기반)
    tilesets_data = {
        'concert_A4_redgreen': {
            'image': 'concert_A4_redgreen.png',
            'name': 'concert_A4_redgreen'
        },
        'concert_B_redgreen': {
            'image': 'concert_B_redgreen.png',
            'name': 'concert_B_redgreen'
        },

        'pixeowl_tiles_free': {
            'image': 'pixeowl_tiles_free.png',
            'name': 'pixeowl_tiles_free'
        },

        'doors': {
            'image': 'doors.png',
            'name': 'doors'
        },

        'concert_D_red': {
            'image': 'concert_D_red.png',
            'name': 'concert_D_red'
        },

        'concert_A2_redgreen': {
            'image': 'concert_A2_redgreen.png',
            'name': 'concert_A2_redgreen'
        },

        'concert_A4': {
            'image': 'concert_A4.png',
            'name': 'concert_A4'
        },

        'office_floors': {
            'image': 'Office_Floors_TILESET_A2.png',
            'name': 'office_floors'
        }
    }
    return tilesets_data