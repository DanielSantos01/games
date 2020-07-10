package principal;

import java.awt.Graphics;
import java.awt.Image;
import java.awt.Rectangle;
import java.io.IOException;
import javax.imageio.ImageIO;

public class Bird {
    protected final Image birdImage[] = new Image[3];
    private final int centery;
    private int flap;
    private final Settings settings;
    private final Ground ground;
    private final Stats stats;
    protected Rectangle rect;
    
    public Bird(Settings set, Ground gnd, Stats stt) throws IOException{
        flap = 0;
        centery = 273;
        rect = new Rectangle(190, centery, 36, 28);
        settings = set;
        ground = gnd;
        stats = stt;
        
        //bird images
        birdImage[0] = ImageIO.read(getClass().getResource("..//assets//bluebird-downflap.png"));
        birdImage[1] = ImageIO.read(getClass().getResource("..//assets//bluebird-midflap.png"));
        birdImage[2] = ImageIO.read(getClass().getResource("..//assets//bluebird-upflap.png"));
    }
    
    public void run(Graphics g){
        draw(g);
        updateWings();
        if(settings.start) updateHeight();
    }
    
    private void updateWings(){
        if(!touchGround()){
            if(flap++ == 2) flap = 0;
        }
    }
    
    private void updateHeight(){
        if(!touchGround()){
            settings.fall += settings.gravity;
            rect.y += settings.fall;
        }else{
            fall("ground");
        }
    }
    
    private void draw(Graphics g){
        g.drawImage(birdImage[flap], rect.x, rect.y, rect.width, rect.height, settings.canvas);
    }
    
    private boolean touchGround(){
        return (rect.y + rect.height) >= (680 - ground.groundImage.getHeight(settings.canvas));
    }
    
    protected void center(){
        rect.y = centery;
    }
    
    protected void fall(String cause){
        switch (cause) {
            case "ground":
                settings.gameOver = true;
                settings.preStart = false;
                settings.start = false;
                settings.configurePipes = true;
                break;
                
            case "pipe":
                settings.gameOver = true;
                break;
                
            default:
                break;
        }
        
        stats.score = 0;
    }
}
