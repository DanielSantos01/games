
package principal;
import java.awt.Graphics;
import java.awt.Image;
import java.awt.Rectangle;
import java.awt.geom.AffineTransform;
import java.awt.image.AffineTransformOp;
import java.awt.image.BufferedImage;
import java.io.IOException;
import javax.imageio.ImageIO;


public class Pipe {
    private Image pipeUpImage;
    private Image pipeDownImage;
    private final Settings settings;
    protected final int pipeUpHight[] = {250, 100, 200, 150, 200, 400, 350, 150, 30, 10};
    protected final int pipeDownHeight[] = {240, 390, 290, 340, 290, 90, 140, 340, 460, 480};
    protected int[] distances = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    private int currentPipe = 0;
    private final Bird bird;
    private final Rectangle rect;
    
    public Pipe(Settings config, Bird brd) throws IOException{
        rect = new Rectangle();
        settings = config;
        configureImages();
        bird = brd;
    }
    
    public void draw(Graphics paintArea){
        if(settings.start || settings.gameOver){
            update(paintArea);
        }else if(settings.preStart && settings.configurePipes){
            configurePipes();
            settings.configurePipes = false;
        }
    }
    
    private void configurePipes(){
        for(int i = 0; i <= 9; i++){
            distances[i] = 450 + 5*i*50;
        }
    }
    
    private void update(Graphics paintArea){
        for(int i = 0; i <= 9; i++){
            updateDownPipes(paintArea, i);
            updateUpPipes(paintArea, i);
            if(!settings.gameOver)distances[i] -= 5;
        }
        checkPipeOut();
    }
    
    private void checkPipeOut(){
        if(distances[currentPipe] == -50){
            distances[currentPipe] = 1950;
            currentPipe++;
            if(currentPipe == 10){
                currentPipe = 0;
            }
        }
    }
    
    private void updateUpPipes(Graphics paintArea, int i){
        paintArea.drawImage(pipeUpImage, distances[i], 680-110 - pipeUpHight[i], 
                pipeUpImage.getWidth(settings.canvas), pipeUpHight[i], settings.canvas);
        rect.x = distances[i];
        rect.y = 680-110 - pipeUpHight[i];
        rect.height = pipeUpHight[i];
        checkCollision(rect);
    }
    
    private void updateDownPipes(Graphics paintArea, int i){
        paintArea.drawImage(pipeDownImage, distances[i], 0, pipeDownImage.getWidth(settings.canvas),
                    pipeDownHeight[i], settings.canvas);
        rect.x = distances[i];
        rect.y = 0;
        rect.height = pipeDownHeight[i];
        checkCollision(rect);
    }
    
    private void configureImages() throws IOException{
        pipeUpImage = ImageIO.read(getClass().getResource("..//assets//pipe-green.png"));
        rect.width = pipeUpImage.getWidth(settings.canvas);
        AffineTransform tx = AffineTransform.getScaleInstance(1, -1);
        tx.translate(0, -pipeUpImage.getHeight(null));
        AffineTransformOp op = new AffineTransformOp(tx, AffineTransformOp.TYPE_NEAREST_NEIGHBOR);
        pipeDownImage = op.filter((BufferedImage)pipeUpImage, null);
    }
    
    public void checkCollision(Rectangle rect){
        if(bird.bird_rect.intersects(rect)){
            bird.loose();
        }
    }
}
