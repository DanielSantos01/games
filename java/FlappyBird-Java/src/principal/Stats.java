package principal;

import java.awt.Graphics;
import java.awt.Image;
import java.io.IOException;
import javax.imageio.ImageIO;

public class Stats {
    private final Image[] number;
    protected int score;
    private final Settings settings;
    private final int height, y, center;
    
    public Stats(Settings set) throws IOException{
        number = new Image[10];
        for(int n = 0; n <= 9; n++) number[n] = ImageIO.read(getClass().getResource("..//assets//"+n+".png"));
        
        score = 0;
        settings = set;
        center = settings.screenWidth/2;
        height = number[1].getHeight(settings.canvas);
        y = 10;
    }
    
    protected void draw(Graphics g){
        if(!(settings.gameOver)){
            if(score < 10) len1(g);
                
            else if(score < 100) len2(g);
                
            else if(score < 1000) len3(g);
        }
    }
    
    private void len1(Graphics g){
        int adjust = number[score].getWidth(settings.canvas);
        g.drawImage(number[score], center-adjust, y, number[score].getWidth(settings.canvas), height, settings.canvas);
    }
    
    private void len2(Graphics g){
        int first = (int) score/10;
        int second = score%10;
        int adjust = number[first].getWidth(settings.canvas);
        g.drawImage(number[first], center-adjust, y, number[first].getWidth(settings.canvas), height, settings.canvas);
                
        adjust = number[second].getWidth(settings.canvas);
        g.drawImage(number[second], (center-adjust)+number[second].getWidth(settings.canvas), y, number[second].getWidth(settings.canvas), height, settings.canvas);
            
    }
    
    private void len3(Graphics g){
        int first = (int) score/100;
        int second = (int) ((score%100)/10);
        int third = (int) ((score%100)%10);
        int adjust = number[first].getWidth(settings.canvas);
        g.drawImage(number[first], center-adjust, y, number[first].getWidth(settings.canvas), height, settings.canvas);
                
        adjust = number[second].getWidth(settings.canvas);
        g.drawImage(number[second], (center-adjust)+number[second].getWidth(settings.canvas), y, number[second].getWidth(settings.canvas), height, settings.canvas);
                
        adjust = number[third].getWidth(settings.canvas);
        g.drawImage(number[third], (center-adjust)+number[second].getWidth(settings.canvas)+number[third].getWidth(settings.canvas), y, number[third].getWidth(settings.canvas), height, settings.canvas);
            
    }
}
