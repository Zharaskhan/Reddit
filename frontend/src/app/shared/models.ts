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
    post_likes: number;
    post_comments: number;
    comments: ICOMMENT[];
}



export interface IAuthResponse {
    token: string;
}


export interface ICOMMENT {
    id: number;
    author: IUser;
    created_at: Date;
    text: string;
    comment_likes: number;
}

