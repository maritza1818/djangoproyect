export interface UserProfile {
    id: number;
    user: {
      id: number;
      username: string;
      email: string;
    };
    birth_date?: string;
    gender?: string;
    favorite_drinks?: string;
    preferred_ambiences?: string;
    personal_phrase?: string;
    profile_picture?: string;
    biography?: string;
    social_media_links?: { [key: string]: string };
    email_notifications: boolean;
    push_notifications: boolean;
    favorite_discos?: number[];
    attended_events?: number[];
    favorite_music?: string;
  }
  