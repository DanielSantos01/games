package breakout;

import java.awt.Graphics2D;
import java.awt.image.BufferStrategy;
import java.io.IOException;
import java.util.ArrayList;

public class RunGame {
    private final Bar bar;
    private final Settings settings;
    private Graphics2D g;
    private final Screen screen;
    private final Ball ball;
    private final ArrayList<Element> wall = new ArrayList();
    private int collide;
    private final Score score;
    private final Button btn;
    
    public RunGame(Bar ba, Settings set, Screen scr, Ball bal, Score scor, Button bt){
        bar = ba;
        settings = set;
        screen = scr;
        ball = bal;
        score = scor;
        btn = bt;
    }
    
    public void render() throws IOException{
        BufferStrategy bs = settings.canvas.getBufferStrategy();
        if(bs == null) {
            settings.canvas.createBufferStrategy(2);
            return;
        }
        g = (Graphics2D) bs.getDrawGraphics();
        
        updateScreen();
        
        g.dispose();
        bs.show();
    }
    
    private void updateScreen() throws IOException{
        screen.fillBackground(g);
        
        bar.draw(g);
        
        ball.execute(g);
        
        if(settings.preStart || settings.gameOver) btn.draw(g);
        if(settings.buildWall) buildWall();
        if(settings.start) checkCollisions();
        
        draWall();
        
        checkLevel();
        score.draw(g);
    }
    
    private void buildWall() throws IOException{
        //row number
        for(int y = 0; y < score.level; y++){
            //elements per row
            for(int x = 0; x <=9; x++){
                Element element = new Element(settings);
                element.rect.x = x*element.rect.width;
                element.rect.y = 30 + y*element.rect.height;
                wall.add(element);
            }
        }
        settings.buildWall = false;
    }
    
    private void checkCollisions(){
        //colisão com a barra
       if(ball.rect.intersects(bar.rect) && settings.start){
           int centerBar = bar.rect.x + (bar.rect.width/2);
           ball.touchBar(centerBar);
       }
       
       //colisão com o muro
       for(Element elm : wall){
           if(ball.rect.intersects(elm.rect)) {
               collide =  wall.indexOf(elm);
               ball.changeDirection();
               score.value += score.level*10;
               settings.remove = true;
               break;
           }
       }
       
       if(settings.remove) removeElement();
    }
    
    private void removeElement(){
        wall.remove(collide);
        settings.remove = false;
    }
    
    private void draWall(){
        wall.stream().forEach((elm) -> {
            elm.draw(g);
        });
    }
    
    private void checkLevel(){
        if(wall.isEmpty()){
            score.level++;
            ball.reset("new level");
            settings.buildWall = true;
        }
        
        if(settings.gameOver){
            wall.clear();
            score.value = 0;
            score.level = 1;
            score.left = 3;
            settings.buildWall = true;
        } 
    }
}
