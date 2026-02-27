#include <raylib.h>

int main()
{
    InitWindow(800, 800, "Simple Trail");
    SetTargetFPS(120);

    int ballx = 400;
    int bally = 400;

    int trailX[10000];
    int trailY[10000];
    int trailCount = 0;

    while (!WindowShouldClose())
    {
        
        if (IsKeyDown(KEY_RIGHT)) ballx += 3;
        if (IsKeyDown(KEY_LEFT))  ballx -= 3;
        if (IsKeyDown(KEY_UP))    bally -= 3;
        if (IsKeyDown(KEY_DOWN))  bally += 3;

        
        if (ballx < 20) ballx = 20;
        if (ballx > 780) ballx = 780;
        if (bally < 20) bally = 20;
        if (bally > 780) bally = 780;

        
        if (trailCount < 10000)
        {
           
            trailX[trailCount] = ballx;
            trailY[trailCount] = bally;
            
            
        }

        BeginDrawing();

        
        ClearBackground(GRAY);
        DrawRectangle(0, 0, 400, 800, BLACK);

        
        for (int i = 0; i < trailCount; i++)
        {
            Color ballcolor = WHITE;

            if (trailX[i] < 395)
                ballcolor = GREEN;
            else if (trailX[i] <= 405)
                ballcolor = BLUE;

            DrawCircle(trailX[i], trailY[i], 20, ballcolor);
        }

        trailCount = (trailCount + 1) % 10000;

        EndDrawing();
    }

    CloseWindow();
    return 0;
}
