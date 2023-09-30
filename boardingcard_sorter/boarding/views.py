# boarding/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class BoardingCardSorter:
    def __init__(self, boardings):
        self.boardings = boardings

    def sort(self):
        # Sort the list of boardings to create a sorted itinerary.
        # Step 1: Get the first and last trip in the itinerary.
        self.set_first_last_boarding()

        # Step 2: Pair boardings based on arrival and departure cities.
        for i in range(len(self.boardings) - 1):
            for idx, trip in enumerate(self.boardings):
                # Check if the arrival city of the current trip matches the departure city of the next trip.
                if self.boardings[i]['arrival'].casefold() == trip['departure'].casefold():
                    # Swap the positions of the current trip and the next trip.Q
                    next_idx = i + 1
                    temp_boarding = self.boardings[next_idx]
                    self.boardings[next_idx] = trip
                    self.boardings[idx] = temp_boarding
        return self.boardings

    def set_first_last_boarding(self):
        # Identify the first and last boarding cards in the itinerary.
        # Initialize flags to track whether the current boarding card is the last or has a previous card.
        is_last_boarding = True
        has_prev_boarding = False

        # Iterate through the list of boarding cards.
        for i in range(len(self.boardings)):
            for trip in self.boardings:
                # Check if the departure city of the current trip matches the arrival city of another trip,
                # indicating that the current trip is not the first in the itinerary.
                if self.boardings[i]['departure'].casefold() == trip['arrival'].casefold():
                    has_prev_boarding = True

                # Check if the arrival city of the current trip matches the departure city of another trip,
                # indicating that the current trip is not the last in the itinerary.
                elif self.boardings[i]['arrival'].casefold() == trip['departure'].casefold():
                    is_last_boarding = False

            # Assign the last and the first trip based on the flags.
            if not has_prev_boarding:
                # It is the first trip, so insert it at the beginning of the list.
                self.boardings.insert(0, self.boardings[i])
                del self.boardings[i]
            elif is_last_boarding:
                # It is the last trip, so append it to the end of the list.
                self.boardings.append(self.boardings[i])
                del self.boardings[i]

        # Remove any None entries created during the boarding card rearrangement.
        self.boardings = [trip for trip in self.boardings if trip is not None]

    def get_boardings(self):
        return self.boardings

class BoardingCardSortView(APIView):
    """
    Sort a list of boarding cards.

    Input format:
    [
        {
            "departure": "Departure location",
            "arrival": "Arrival location",
            "transportation": "Type of transportation",
            "gate": "Gate information (optional)",
            "seat": "Seat assignment (optional)",
            "additional_info": "Additional information (optional)"
        },
        ...
    ]
    """
    def post(self, request, format=None):
        # Get the list of boarding cards from the request data
        boarding_cards = request.data

        # Create a BoardingCardSorter instance and sort the boarding cards
        sorter = BoardingCardSorter(boarding_cards)
        sorted_boarding_cards = sorter.sort()
        print(sorted_boarding_cards)

        # Generate step-by-step descriptions
        sorted_descriptions = self.generate_descriptions(sorted_boarding_cards)

        return Response({'sorted_boarding_cards': sorted_descriptions}, status=status.HTTP_200_OK)

    def generate_descriptions(self, boarding_cards):
        # Generate step-by-step descriptions for the sorted boarding cards
        descriptions = []
        for idx, card in enumerate(boarding_cards):
            description = f"{idx + 1}. Take {card['transportation']} from {card['departure']} to {card['arrival']}."

            if card.get('gate'):
                description += f" Gate {card['gate']}."

            if card.get('seat'):
                description += f" Sit in seat {card['seat']}."

            if card.get('additional_info'):
                description += f" {card['additional_info']}"

            descriptions.append(description)

        # Add a final arrival message
        descriptions.append(f"{len(boarding_cards) + 1}. You have arrived at your final destination.")

        return descriptions