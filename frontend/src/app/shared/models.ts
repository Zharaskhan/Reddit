export interface IUser {
    id: number;
    username: string;
}

export interface IPOST {
    id: number;
    author: IUser;
    created_at: Date;
    title: string;
    body: string;
}

export interface IAuthResponse {
    token: string;
}

