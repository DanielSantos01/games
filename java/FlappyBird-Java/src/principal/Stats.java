package principal;

import java.awt.Graphics;
import java.awt.Image;
import java.io.IOException;
import javax.imageio.ImageIO;

public class Stats {
    private final Image[] number;
    protected int score;
    private final Settings settings;
    private final int width;
    private final int height;
    private final int center;
    
    public Stats(Settings set) throws IOException{
        number = new Image[10];
        score = 0;
        settings = set;
        for(int n = 0; n <= 9; n++){
            number[n] = ImageIO.read(getClass().getResource("..//assets//"+n+".png"));
        }
        width = number[0].getWidth(settings.canvas);
        height = number[0].getHeight(settings.canvas);
        center = (settings.screenWidth/2) - (width/2);
    }
    
    protected void draw(Graphics g){
        if(!(settings.gameOver)){
            if(score < 10){
                g.drawImage(number[score], center, 10, number[score].getWidth(settings.canvas), height, settings.canvas);
            
            }else if(score < 100){
                int first = (int) score/10;
                int second = score%10;
                g.drawImage(number[first], center, 10, number[first].getWidth(settings.canvas), height, settings.canvas);
                g.drawImage(number[second], center+number[second].getWidth(settings.canvas), 10, number[second].getWidth(settings.canvas), height, settings.canvas);
            
            }else if(score < 1000){
                int first = (int) score/100;
                int second = (int) ((score%100)/10);
                int third = (int) ((score%100)%10);
                g.drawImage(number[first], center, 10, number[first].getWidth(settings.canvas), height, settings.canvas);
                g.drawImage(number[second], center+number[second].getWidth(settings.canvas), 10, number[second].getWidth(settings.canvas), height, settings.canvas);
                g.drawImage(number[third], center+number[second].getWidth(settings.canvas)+number[third].getWidth(settings.canvas), 10, number[third].getWidth(settings.canvas), height, settings.canvas);
            }
        }
    }
}
