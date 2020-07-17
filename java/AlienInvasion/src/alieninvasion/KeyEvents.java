package alieninvasion;

import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;


public class KeyEvents implements KeyListener{
    private final Ship ship;
    private final Settings settings;
    
    public KeyEvents(Ship shp, Settings set){
        ship = shp;
        settings = set;
    }

    @Override
    public void keyTyped(java.awt.event.KeyEvent ke) {}

    @Override
    public void keyPressed(java.awt.event.KeyEvent ke) {
        switch(ke.getKeyCode()){
            case KeyEvent.VK_LEFT:
                if(ship.rect.x > 0) ship.rect.x -= 10;
                break;
                
            case KeyEvent.VK_RIGHT:
                if((ship.rect.x + ship.rect.width) < settings.screenWidth) ship.rect.x += 10;
                break;
                
            case KeyEvent.VK_SPACE:
                if(settings.preStart){
                    settings.preStart = false;
                    settings.start = true;
                    settings.gameOver = false;
                    
                }else if(settings.start){
                    settings.shoot = true;
                    
                }else{
                    settings.preStart = true;
                }
                break;
        }
    }
   
    @Override
    public void keyReleased(java.awt.event.KeyEvent ke) {
        
    }
    
}
