from marshmallow import Schema, fields, post_load


# class EventMeeting(ContractBase):
#     definition = {
#         'id': IntegerField,
#         'date': DateTimeField(dt_format='iso8601'),
#         'endDate': DateTimeField(dt_format='iso8601'),
#         'title': StringField,
#         'description': StringField,
#         'privacy': StringField,
#         'organizer': fields.Nested(Organizer.definition),
#         'rsvps': fields.Nested(RSVPStatDetailed.definition),
#         'venue': fields.Nested(Venue.definition, allow_null=True),
#         'eventType': StringField,
#         'isManager': BooleanField,
#         'isMember': BooleanField,
#         'permaLink': StringField,
#         'recurrence': StringField
#     }
#
#     def __init__(self):
#         self.id = None
#         self.date = None
#         self.end_date = None
#         self.title = None
#         self.description = None
#         self.privacy = None
#         self.organizer = Organizer()
#         self.rsvps = RSVPStatDetailed()
#         self.venue = None
#         self.event_type = None
#         self.is_manager = None
#         self.is_member = None
#         self.perma_link = None
#         self.recurrence = None
#
#
# class EventPickup(ContractBase):
#     definition = {
#         'id': IntegerField,
#         'date': DateTimeField(dt_format='iso8601'),
#         'endDate': DateTimeField(dt_format='iso8601'),
#         'title': StringField,
#         'description': StringField,
#         'privacy': StringField,
#         'organizer': fields.Nested(Organizer.definition),
#         'venue': fields.Nested(Venue.definition, allow_null=True),
#         'field': fields.Nested(Field.definition, allow_null=True),
#         'rsvps': fields.Nested(RSVPStatDetailed.definition),
#         'eventType': StringField,
#         'isManager': BooleanField,
#         'permaLink': StringField,
#         'recurrence': StringField
#     }
#
#     def __init__(self):
#         self.id = None
#         self.date = None
#         self.end_date = None
#         self.title = None
#         self.description = None
#         self.privacy = None
#         self.organizer = Organizer()
#         self.rsvps = RSVPStatDetailed()
#         self.venue = None
#         self.event_type = None
#         self.is_manager = None
#         self.field = None
#         self.perma_link = None
#         self.recurrence = None


# class EventGame(ContractBase):
#     definition = {
#         'id': IntegerField,
#         'eventType': StringField,
#         'date': DateTimeField(dt_format='iso8601'),
#         'competition': fields.Nested(CompetitionSummary.definition, allow_null=True),
#         'division': fields.Nested(Division.definition, allow_null=True),
#         'season': fields.Nested(Season.definition, allow_null=True),
#         'awayTeam': fields.Nested(TeamShortSummary.definition),
#         'homeTeam': fields.Nested(TeamShortSummary.definition),
#         'currentTeam': fields.Nested(TeamShortSummary.definition, allow_null=True),
#         'venue': fields.Nested(Venue.definition, allow_null=True),
#         'field': fields.Nested(Field.definition, allow_null=True),
#         'rsvps': fields.Nested(RSVPStatDetailed.definition),
#         'isCompetitionManager': BooleanField,
#         'isHomeManager': BooleanField,
#         'isAwayManager': BooleanField,
#         'isHomeMember': BooleanField,
#         'isAwayMember': BooleanField,
#         "postponed": BooleanField,
#         "played": BooleanField,
#         "homeScore": IntegerField,
#         "awayScore": IntegerField,
#         "hasPenalties": BooleanField,
#         "homePenalScore": IntegerField,
#         "awayPenalScore": IntegerField,
#         "homeForfeit": BooleanField,
#         "awayForfeit": BooleanField,
#         'homeTeamForm': fields.List(StringField),
#         'awayTeamForm': fields.List(StringField),
#         'isProfessional': BooleanField,
#         'gameMinute': StringField,
#         'gameStatus': StringField,
#         'round': StringField,
#         'roundId': IntegerField,
#         'permaLink': StringField,
#         'locked': BooleanField
#     }
#
#     def __init__(self):
#         self.id = None
#         self.event_type = None
#         self.competition = None
#         self.division = None
#         self.season = None
#         self.is_competition_manager = None
#         self.is_home_manager = None
#         self.is_away_manager = None
#         self.is_home_member = None
#         self.is_away_member = None
#         self.date = None
#         self.home_team = TeamShortSummary()
#         self.away_team = TeamShortSummary()
#         self.current_team = None
#         self.venue = None
#         self.rsvps = RSVPStatDetailed()
#         self.postponed = None
#         self.played = None
#         self.home_score = None
#         self.away_score = None
#         self.has_penalties = None
#         self.home_penal_score = None
#         self.away_penal_score = None
#         self.home_forfeit = None
#         self.away_forfeit = None
#         self.home_team_form = []
#         self.away_team_form = []
#         self.field = None
#         self.is_professional = None
#         self.game_minute = None
#         self.game_status = None
#         self.round = None
#         self.round_id = None
#         self.perma_link = None
#         self.locked = False


# class TeamShortSummary(ContractBase):
#     definition = {
#         'id': IntegerField,
#         'name': StringField,
#         'initials': StringField,
#         'crestPicture': fields.Nested(Picture.definition, allow_null=True),
#         'coverPhoto': fields.Nested(Picture.definition, allow_null=True),
#         'username': StringField,
#         'permaLink': StringField
#     }
#
#     def __init__(self):
#         self.id = None
#         self.name = None
#         self.initials = None
#         self.crest_picture = None
#         self.cover_photo = None
#         self.username = None
#         self.perma_link = None


# class EventPractice(Schema):
#     definition = {
#         'id': IntegerField,
#         'date': DateTimeField(dt_format='iso8601'),
#         'endDate': DateTimeField(dt_format='iso8601'),
#         'team': fields.Nested(TeamShortSummary.definition),
#         'venue': fields.Nested(Venue.definition, allow_null=True),
#         'field': fields.Nested(Field.definition, allow_null=True),
#         'description': StringField,
#         'rsvps': fields.Nested(RSVPStatDetailed.definition),
#         'privacy': StringField,
#         'eventType': StringField,
#         'isManager': BooleanField,
#         'isMember': BooleanField,
#         'permaLink': StringField,
#         'recurrence': StringField
#     }
#
#     def __init__(self):
#         self.id = None
#         self.date = None
#         self.end_date = None
#         self.team = TeamShortSummary()
#         self.venue = None
#         self.description = None
#         self.rsvps = RSVPStatDetailed()
#         self.privacy = None
#         self.event_type = None
#         self.is_manager = None
#         self.is_member = None
#         self.field = None
#         self.perma_link = None
#         self.recurrence = None
