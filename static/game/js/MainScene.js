export default class MainScene extends Phaser.Scene {
    constructor(){
        super("MainScene");
    }

    // 이미지 자원의 경로 문제 존재 (HTTP 404 Not Found 에러)
    preload() {
        console.log("preload");
        this.load.atlas('man','../assets/images/man.png','../assets/images/man_atlas.json');
        this.load.animation('man_anim','../assets/images/man_anim.json');
    }

    create() {
        console.log("create");
        this.player = new Phaser.Physics.Matter.Sprite(this.matter.world,0,0,'man','townsfolk_m_idle_1');
        this.add.existing(this.player);
        this.inputKeys = this.input.keyboard.addKeys({
            up: Phaser.Input.Keyboard.KeyCodes.W,
            down: Phaser.Input.Keyboard.KeyCodes.S,
            left: Phaser.Input.Keyboard.KeyCodes.A,
            right: Phaser.Input.Keyboard.KeyCodes.D,
        });
    }
    
    update() {
        this.player.anims.play('man_walk',true);
        const speed = 2.5;
        let playerVelocity = new Phaser.Math.Vector2();
        if (this.inputKeys.left.isDown) {
            playerVelocity.x = -1;
        } else if (this.inputKeys.right.isDown) {
            playerVelocity.x = 1;
        }
        if (this.inputKeys.up.isDown) {
            playerVelocity.y = -1;
        } else if (this.inputKeys.down.isDown) {
            playerVelocity.y = 1;
        }
        playerVelocity.normalize().scale(speed);
        this.player.setVelocity(playerVelocity.x, playerVelocity.y);
    }
}