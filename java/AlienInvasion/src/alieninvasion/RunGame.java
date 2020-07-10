package alieninvasion;

import java.awt.Graphics2D;
import java.awt.image.BufferStrategy;

public class RunGame {
    private final Screen screen;
    private final Settings settings;
    private final Ship ship;
    private Graphics2D g;
    
    public RunGame(Screen scr, Settings set, Ship shp){
        screen = scr;
        settings = set;
        ship = shp;
    }
    
    protected void start(){
        while(true) update();
    }
    
    private void update(){
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
    
    private void updateScreen(){
        settings.clock(30);
        screen.fill(g);
        ship.run(g);
    }
}
