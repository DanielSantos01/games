package principal;
import java.awt.Graphics;
import java.awt.Image;
import java.awt.Rectangle;
import java.io.IOException;
import javax.imageio.ImageIO;

public class Bird {
    protected final Image birdImage[] = new Image[3];
    private int numberImage = 0;
    protected Rectangle bird_rect;
    private Settings settings;
    private Ground ground;
    
    public Bird(Settings config, Ground chaozinho) throws IOException{
        settings = config;
        ground = chaozinho;
        bird_rect = new Rectangle(190, 273, 36, 28);
        birdImage[0] = ImageIO.read(getClass().getResource("..//assets//bluebird-upflap.png"));
        birdImage[1] = ImageIO.read(getClass().getResource("..//assets//bluebird-midflap.png"));
        birdImage[2] = ImageIO.read(getClass().getResource("..//assets//bluebird-downflap.png"));
    }
    
    public void run(Graphics g){
        if(settings.preStart){
            drawBird(g);
            updateImage(); 
        }else if(settings.start){
            drawBird(g);
            updateBirdHeight();
            updateImage();
        }else{
            drawBird(g);
        } 
    }
    
    private void updateImage(){
        numberImage++;
        if(numberImage == 3) numberImage = 0;
    }
    
    private void updateBirdHeight(){
        if(!touchGround()){
            settings.fall += settings.gravity;
            bird_rect.y += settings.fall;
        }else{
            settings.gameOver = true;
            settings.preStart = false;
            settings.start = false;
        }
    }
    
    private void drawBird(Graphics g){
        g.drawImage(birdImage[numberImage], bird_rect.x, bird_rect.y, bird_rect.width, bird_rect.height, settings.canvas);
    }
    
    private boolean touchGround(){
        return (bird_rect.y + bird_rect.height) >= (680 - ground.ground.getHeight(settings.canvas));
    }
    
    protected void centerBird(){
        bird_rect.y = 273;
    }
    
    protected void loose(){
        
    }
}
