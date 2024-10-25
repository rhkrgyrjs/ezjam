// 메인 타일맵 생성 함수 (맵마다 다르게 짜야함)
function createMainTileMap() {
    const map = this.make.tilemap({ key: 'main' });

    // 타일셋을 로드한 후 타일셋과 레이어 연결
    const tilesetConcertRedGreenB = map.addTilesetImage('concert_B_redgreen', 'concert_B_redgreen', 32, 32);
    const tilesetConcertRedD = map.addTilesetImage('concert_D_red', 'concert_D_red', 32, 32);
    const tilesetPixowl = map.addTilesetImage('pixeowl_tiles_free', 'pixeowl_tiles_free', 32, 32);
    const tilesetConcertRedGreenA4 = map.addTilesetImage('concert_A4_redgreen', 'concert_A4_redgreen', 32, 32);

    // 레이어 생성
    this.groundLayer = map.createLayer('ground', tilesetPixowl, 0, 0);
    this.building1Layer = map.createLayer('building_1', tilesetConcertRedGreenA4, 0, 0);
    this.tileLayer = map.createLayer('tile', tilesetPixowl, 0, 0);
    this.signLayer = map.createLayer('sign', [tilesetConcertRedGreenB, tilesetConcertRedD], 0, 0);
    this.extraLayer = map.createLayer('extra', [tilesetConcertRedD, tilesetConcertRedGreenB], 0, 0);

    console.log(map.layers);
    console.log(this.groundLayer, this.tileLayer, this.building1Layer, this.signLayer, this.extraLayer);

    // 충돌 가능한 타일 설정
    [this.groundLayer, this.tileLayer, this.building1Layer, this.signLayer, this.extraLayer].forEach(layer => {
        layer.setCollisionByProperty({ collides: true });
    });

    // 충돌 설정 함수 호출
    setupCollidersMain.call(this);
}

// 충돌 설정 함수
function setupCollidersMain() {
    // 플레이어와 레이어 간의 충돌 설정
    this.physics.add.collider(player, this.groundLayer, onCollision, null, this);
    this.physics.add.collider(player, this.tileLayer, onCollision, null, this);
    this.physics.add.collider(player, this.building1Layer, onCollision, null, this);
    this.physics.add.collider(player, this.signLayer, onCollision, null, this);
    this.physics.add.collider(player, this.extraLayer, onCollision, null, this);
}



// 로비 타일맵 생성 함수 (맵마다 다르게 짜야함)
function createLobbyTileMap() {
    const map = this.make.tilemap({ key: 'lobby' });

    // 타일셋을 로드한 후 타일셋과 레이어 연결
    const tilesetConcertRedGreenB = map.addTilesetImage('concert_B_redgreen', 'concert_B_redgreen', 32, 32);
    const tilesetDoor = map.addTilesetImage('doors', 'doors', 32, 32);
    const tilestConcertA4 = map.addTilesetImage('concert_A4', 'concert_A4', 32, 32);

    // 레이어 생성
    this.floorLayer = map.createLayer('floor', tilestConcertA4, 0, 0);
    this.wallLayer = map.createLayer('wall', tilestConcertA4, 0, 0);
    this.extraLayer = map.createLayer('extra', tilesetConcertRedGreenB, 0, 0);
    this.doorLayer = map.createLayer('door', tilesetDoor, 0, 0);

    // 충돌 가능한 타일 설정
    [this.extraLayer, this.doorLayer, this.wallLayer, this.floorLayer].forEach(layer => {
        layer.setCollisionByProperty({ collides: true });
    });

    // 충돌 설정 함수 호출
    setupCollidersLobby.call(this);
}

// 힙합 충돌 설정 함수
function setupCollidersLobby() {
    // 플레이어와 레이어 간의 충돌 설정
    this.physics.add.collider(player, this.extraLayer, onCollision, null, this);
    this.physics.add.collider(player, this.doorLayer, onCollision, null, this);
    this.physics.add.collider(player, this.wallLayer, onCollision, null, this);
    this.physics.add.collider(player, this.floorLayer, onCollision, null, this);
}




// 힙합 타일맵 생성 함수 (맵마다 다르게 짜야함)
function createHiphopTileMap() {
    const map = this.make.tilemap({ key: 'hiphop' });

    // 타일셋을 로드한 후 타일셋과 레이어 연결
    const tilesetA = map.addTilesetImage('concert_A4_redgreen', 'concert_A4_redgreen', 32, 32);
    const tilesetB = map.addTilesetImage('concert_B_redgreen', 'concert_B_redgreen', 32, 32);

    // 레이어 생성
    this.floorLayer = map.createLayer('floor', tilesetA, 0, 0);
    this.secondFloorLayer = map.createLayer('2floor', tilesetB, 0, 0);
    this.extraLayer = map.createLayer('extra', tilesetB, 0, 0);

    // 충돌 가능한 타일 설정
    [this.floorLayer, this.secondFloorLayer, this.extraLayer].forEach(layer => {
        layer.setCollisionByProperty({ collides: true });
    });

    // 충돌 설정 함수 호출
    setupCollidersHiphop.call(this);
}

// 힙합 충돌 설정 함수
function setupCollidersHiphop() {
    // 플레이어와 레이어 간의 충돌 설정
    this.physics.add.collider(player, this.floorLayer, onCollision, null, this);
    this.physics.add.collider(player, this.secondFloorLayer, onCollision, null, this);
    this.physics.add.collider(player, this.extraLayer, onCollision, null, this);
}



// 락 타일맵 생성 함수 (맵마다 다르게 짜야함)
function createRockTileMap() {
    const map = this.make.tilemap({ key: 'rock' });

    // 타일셋을 로드한 후 타일셋과 레이어 연결
    const tilesetConcertRedGreenB = map.addTilesetImage('concert_B_redgreen', 'concert_B_redgreen', 32, 32);
    const tilesetConcertRedGreenA4 = map.addTilesetImage('concert_A4_redgreen', 'concert_A4_redgreen', 32, 32);
    const tilesetOfficefloor = map.addTilesetImage('office_floors', 'office_floors', 32, 32);

    // 레이어 생성
    this.floorLayer = map.createLayer('floor', tilesetOfficefloor, 0, 0);
    this.secondFloorLayer = map.createLayer('2floor', [tilesetConcertRedGreenB, tilesetConcertRedGreenA4], 0, 0);
    this.extraLayer = map.createLayer('extra', tilesetConcertRedGreenB, 0, 0);

    // 충돌 설정 함수 호출
    setupCollidersRock.call(this);
}

// 락 충돌 설정 함수
function setupCollidersRock() {
    // 플레이어와 레이어 간의 충돌 설정
    this.physics.add.collider(player, this.floorLayer, onCollision, null, this);
    this.physics.add.collider(player, this.secondFloorLayer, onCollision, null, this);
    this.physics.add.collider(player, this.extraLayer, onCollision, null, this);
}


// 발라드 타일맵 생성 함수 (맵마다 다르게 짜야함)
function createBalladTileMap() {
    const map = this.make.tilemap({ key: 'ballad' });

    // 타일셋을 로드한 후 타일셋과 레이어 연결
    const tilesetConcertRedGreenB = map.addTilesetImage('concert_B_redgreen', 'concert_B_redgreen', 32, 32);
    const tilesetConcertRedGreenA4 = map.addTilesetImage('concert_A4_redgreen', 'concert_A4_redgreen', 32, 32);

    // 레이어 생성
    this.floorLayer = map.createLayer('floor', tilesetConcertRedGreenA4, 0, 0);
    this.secondFloorLayer = map.createLayer('2floor', [tilesetConcertRedGreenB, tilesetConcertRedGreenA4], 0, 0);
    this.extraLayer = map.createLayer('extra', tilesetConcertRedGreenB, 0, 0);

    // 충돌 설정 함수 호출
    setupCollidersBallad.call(this);
}

// 발라드 충돌 설정 함수
function setupCollidersBallad() {
    // 플레이어와 레이어 간의 충돌 설정
    this.physics.add.collider(player, this.floorLayer, onCollision, null, this);
    this.physics.add.collider(player, this.secondFloorLayer, onCollision, null, this);
    this.physics.add.collider(player, this.extraLayer, onCollision, null, this);
}


// 인디 타일맵 생성 함수 (맵마다 다르게 짜야함)
function createIndiTileMap() {
    const map = this.make.tilemap({ key: 'indi' });

    // 타일셋추가// 타일셋을 로드한 후 타일셋과 레이어 연결
    const tilesetConcertRedGreenB = map.addTilesetImage('concert_B_redgreen', 'concert_B_redgreen', 32, 32);
    const tilesetConcertRedGreenA4 = map.addTilesetImage('concert_A4_redgreen', 'concert_A4_redgreen', 32, 32);
    const tilesetPixowl = map.addTilesetImage('pixeowl_tiles_free', 'pixeowl_tiles_free', 32, 32);

    this.floorLayer = map.createLayer('floor', tilesetPixowl, 0, 0);
    this.secondFloorLayer = map.createLayer('2floor', [tilesetConcertRedGreenB, tilesetConcertRedGreenA4], 0, 0);
    this.extraLayer = map.createLayer('extra', tilesetConcertRedGreenB, 0, 0);

    // 충돌 설정 함수 호출
    setupCollidersIndi.call(this);
}

// 인디 충돌 설정 함수
function setupCollidersIndi() {
    // 플레이어와 레이어 간의 충돌 설정
    this.physics.add.collider(player, this.floorLayer, onCollision, null, this);
    this.physics.add.collider(player, this.secondFloorLayer, onCollision, null, this);
    this.physics.add.collider(player, this.extraLayer, onCollision, null, this);

}


// 충돌 발생 시 호출되는 함수
function onCollision() {
    console.log('충돌 발생!');
}