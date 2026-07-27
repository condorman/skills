import 'package:flame/game.dart';
import 'package:flutter_test/flutter_test.dart';

import 'package:battleshipspro/game/battleships_game.dart';
import 'package:battleshipspro/models/upgrade_card.dart';

void main() {
  TestWidgetsFlutterBinding.ensureInitialized();

  group('Battleships Pro Game Design & Balance Simulation Suite', () {
    testWidgets('Simulate 10 Matches with Full Flame Engine & Evaluate Gameplay Metrics', (WidgetTester tester) async {
      int victories = 0;
      int defeats = 0;
      int totalLevelUps = 0;
      double totalGameSeconds = 0.0;

      for (int matchIndex = 1; matchIndex <= 10; matchIndex++) {
        final game = BattleshipsGame();

        // Attach Flame Game to Widget Tree so World and components mount cleanly
        await tester.pumpWidget(GameWidget(game: game));
        await tester.pump();
        await game.ready();

        // Enable Auto-Pilot AI for Player Ship
        game.player.isAutoPilotEnabled = true;

        // Auto-select upgrades on level up during simulation
        game.onLevelUp = () {
          totalLevelUps++;
          final card = UpgradeCard.allUpgrades[matchIndex % UpgradeCard.allUpgrades.length];
          if (card.type == UpgradeType.weapon) {
            game.player.stats.fireRate += 0.5;
          }
          game.player.stats.maxHealth += 20.0;
          game.player.stats.health += 20.0;
          game.resumeGame();
        };

        // Simulate match ticks synchronously (up to 180 seconds of game time per match)
        const double dt = 0.1; // 10 FPS step
        int ticks = 0;
        const int maxTicks = 1800; // 180 seconds

        while (!game.isGameOver && ticks < maxTicks) {
          game.update(dt);
          ticks++;
        }

        final double matchDurationSec = ticks * dt;
        totalGameSeconds += matchDurationSec;

        if (game.isVictory) {
          victories++;
        } else {
          defeats++;
        }

        // Print simulation summary for this match
        // ignore: avoid_print
        print('Match #$matchIndex Result: ${game.isVictory ? "VICTORY" : "DEFEAT"} | Kills: ${game.killsCount} | Score: ${game.score} | Level: ${game.currentLevel} | Duration: ${matchDurationSec.toStringAsFixed(1)}s');
      }

      final double winRatePercent = (victories / 10) * 100;
      final double avgDurationSec = totalGameSeconds / 10;

      // ignore: avoid_print
      print('=== GAME DESIGN BALANCING SIMULATION REPORT ===');
      // ignore: avoid_print
      print('Total Victories: $victories / 10 ($winRatePercent%)');
      // ignore: avoid_print
      print('Average Match Duration: ${avgDurationSec.toStringAsFixed(1)}s');
      // ignore: avoid_print
      print('Total Level-Ups Triggered: $totalLevelUps');

      expect(victories + defeats, equals(10));
    });
  });
}
