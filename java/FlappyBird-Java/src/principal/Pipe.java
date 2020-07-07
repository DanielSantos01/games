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
    protected int[] x = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    private int currentPipe = 0;
    private final Bird bird;
    private final Rectangle rect;
    
    public Pipe(Settings set, Bird brd) throws IOException{
        rect = new Rectangle();
        settings = set;
        configureImages();
        rect.width = pipeUpImage.getWidth(settings.canvas);
        bird = brd;
    }
    
    public void draw(Graphics g){
        
        if(settings.start || settings.gameOver) show(g);
        else if(settings.preStart && settings.configurePipes) configurePipes();
        
    }
    
    private void configurePipes(){
        
        for(int pipe = 0; pipe <= 9; pipe++) x[pipe] = 450 + 4*pipe*50;
        
        settings.configurePipes = false;
    }
    
    private void show(Graphics g){
        for(int pipe = 0; pipe <= 9; pipe++){
            showDownPipes(g, pipe);
            checkCollision(rect);
            
            showUpPipes(g, pipe);
            checkCollision(rect);
            
            updatePosition(pipe);
        }
        checkPipeOut();
    }
    
    private void updatePosition(int pipe){
        if(!settings.gameOver) x[pipe] -= 5;
    }
    
    private void checkPipeOut(){
        if(x[currentPipe] == -50){
            x[currentPipe] = 1950;
            currentPipe++;
            if(currentPipe == 10) currentPipe = 0;
        }
    }
    
    private void showUpPipes(Graphics g, int pipe){
        g.drawImage(pipeUpImage, x[pipe], 680-110 - pipeUpHight[pipe], pipeUpImage.getWidth(settings.canvas), pipeUpHight[pipe], settings.canvas);
        rect.x = x[pipe];
        rect.y = 680-110 - pipeUpHight[pipe];
        rect.height = pipeUpHight[pipe];
    }
    
    private void showDownPipes(Graphics g, int pipe){
        g.drawImage(pipeDownImage, x[pipe], 0, pipeDownImage.getWidth(settings.canvas), pipeDownHeight[pipe], settings.canvas);
        rect.x = x[pipe];
        rect.y = 0;
        rect.height = pipeDownHeight[pipe];
    }
    
    private void configureImages() throws IOException{
        pipeUpImage = ImageIO.read(getClass().getResource("..//assets//pipe-green.png"));
        AffineTransform tx = AffineTransform.getScaleInstance(1, -1);
        tx.translate(0, -pipeUpImage.getHeight(null));
        AffineTransformOp op = new AffineTransformOp(tx, AffineTransformOp.TYPE_NEAREST_NEIGHBOR);
        pipeDownImage = op.filter((BufferedImage)pipeUpImage, null);
    }
    
    public void checkCollision(Rectangle rect){
        if(bird.rect.intersects(rect)) bird.fall("pipe");
    }
}
