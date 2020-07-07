package principal;

import java.awt.Graphics;
import java.awt.Image;
import java.awt.Rectangle;
import java.io.IOException;
import javax.imageio.ImageIO;

public class Bird {
    protected final Image birdImage[] = new Image[3];
    private final int centery;
    private int numberImage = 0;
    protected Rectangle rect;
    private final Settings settings;
    private final Ground ground;
    
    public Bird(Settings set, Ground gnd) throws IOException{
        settings = set;
        ground = gnd;
        rect = new Rectangle(190, 273, 36, 28);
        centery = 273;
        birdImage[0] = ImageIO.read(getClass().getResource("..//assets//bluebird-upflap.png"));
        birdImage[1] = ImageIO.read(getClass().getResource("..//assets//bluebird-midflap.png"));
        birdImage[2] = ImageIO.read(getClass().getResource("..//assets//bluebird-downflap.png"));
    }
    
    public void run(Graphics g){
        draw(g);
        updateWings();
        if(settings.start) updateBirdHeight();
    }
    
    private void updateWings(){
        if(!touchGround()){
            numberImage++;
            if(numberImage == 3) numberImage = 0;
        }
    }
    
    private void updateBirdHeight(){
        if(!touchGround()){
            settings.fall += settings.gravity;
            rect.y += settings.fall;
        }else{
            fall("ground");
        }
    }
    
    private void draw(Graphics g){
        g.drawImage(birdImage[numberImage], rect.x, rect.y, rect.width, rect.height, settings.canvas);
    }
    
    private boolean touchGround(){
        return (rect.y + rect.height) >= (680 - ground.groundImage.getHeight(settings.canvas));
    }
    
    protected void centerBird(){
        rect.y = centery;
    }
    
    protected void fall(String cause){
        switch (cause) {
            case "ground":
                settings.gameOver = true;
                settings.preStart = false;
                settings.start = false;
                settings.configurePipes = true;
                settings.touchPipe = false;
                break;
            case "pipe":
                settings.touchPipe = true;
                settings.gameOver = true;
                break;
        }
    }
}
