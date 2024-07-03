from django.db import models


# class Game(models.Model):
#     player1 = models.ForeignKey(User, related_name='player1_games', on_delete=models.CASCADE)
#     player2 = models.ForeignKey(User, related_name='player2_games', on_delete=models.CASCADE, null=True, blank=True)
#     winner = models.ForeignKey(User, related_name='won_games', on_delete=models.CASCADE, null=True, blank=True)
#     against_bot = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         if self.against_bot:
#             player2_name = "Bot"
#         else:
#             player2_name = self.player2.username if self.player2 else "Unknown"
#         winner_name = self.winner.username if self.winner else "No Winner"
#         return f"Game between {self.player1.username} and {player2_name}. Winner: {winner_name}"

#     def get_winner_display(self):
#         return self.winner.username if self.winner else "Draw"

